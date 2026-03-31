from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

from .models import (
    Category, Product, Cart, CartItem, Order, OrderItem,
    Review, Wishlist, Newsletter, SkinQuiz, Coupon, SiteSettings
)


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Merge session cart if exists
        if request.session.session_key:
            try:
                session_cart = Cart.objects.get(session_key=request.session.session_key, user=None)
                for item in session_cart.items.all():
                    cart_item, ci_created = CartItem.objects.get_or_create(
                        cart=cart, product=item.product,
                        defaults={'quantity': item.quantity}
                    )
                    if not ci_created:
                        cart_item.quantity += item.quantity
                        cart_item.save()
                session_cart.delete()
            except Cart.DoesNotExist:
                pass
        return cart
    else:
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key, user=None)
        return cart


# ─── HOME ───────────────────────────────────────────────────────────────────────
def home(request):
    settings = SiteSettings.get_settings()
    featured = Product.objects.filter(is_featured=True, is_active=True)[:8]
    bestsellers = Product.objects.filter(is_bestseller=True, is_active=True)[:4]
    new_arrivals = Product.objects.filter(is_new_arrival=True, is_active=True)[:4]
    categories = Category.objects.filter(is_active=True)[:6]
    recent_reviews = Review.objects.filter(is_approved=True).select_related('user', 'product')[:6]
    
    context = {
        'settings': settings,
        'featured': featured,
        'bestsellers': bestsellers,
        'new_arrivals': new_arrivals,
        'categories': categories,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'store/home.html', context)


# ─── SHOP / PRODUCT LIST ─────────────────────────────────────────────────────────
def shop(request):
    products = Product.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.filter(is_active=True)
    
    # Filters
    category_slug = request.GET.get('category')
    skin_type = request.GET.get('skin_type')
    sort = request.GET.get('sort', 'newest')
    q = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    show_natural = request.GET.get('natural')
    
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
    
    if skin_type:
        products = products.filter(skin_type=skin_type)
    
    if q:
        products = products.filter(
            Q(name__icontains=q) |
            Q(brand__icontains=q) |
            Q(description__icontains=q) |
            Q(category__name__icontains=q)
        )
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    if show_natural:
        products = products.filter(is_natural=True)
    
    # Sort
    sort_map = {
        'newest': '-created_at',
        'oldest': 'created_at',
        'price_low': 'price',
        'price_high': '-price',
        'popular': '-views',
        'name': 'name',
    }
    products = products.order_by(sort_map.get(sort, '-created_at'))
    
    paginator = Paginator(products, 12)
    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)
    
    context = {
        'products': products_page,
        'categories': categories,
        'selected_category': selected_category,
        'skin_type': skin_type,
        'sort': sort,
        'q': q,
        'total_count': paginator.count,
    }
    return render(request, 'store/shop.html', context)


# ─── PRODUCT DETAIL ───────────────────────────────────────────────────────────────
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    product.views += 1
    product.save(update_fields=['views'])
    
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:4]
    
    reviews = product.reviews.filter(is_approved=True).select_related('user')
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()
    
    context = {
        'product': product,
        'related': related,
        'reviews': reviews,
        'user_review': user_review,
        'in_wishlist': in_wishlist,
    }
    return render(request, 'store/product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    
    sort = request.GET.get('sort', 'newest')
    sort_map = {'newest': '-created_at', 'price_low': 'price', 'price_high': '-price', 'popular': '-views'}
    products = products.order_by(sort_map.get(sort, '-created_at'))
    
    paginator = Paginator(products, 12)
    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)
    
    context = {
        'category': category,
        'products': products_page,
        'sort': sort,
    }
    return render(request, 'store/category_detail.html', context)


# ─── CART ─────────────────────────────────────────────────────────────────────────
def cart(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related('product').all()
    settings = SiteSettings.get_settings()
    
    delivery_fee = 0
    if cart.total < settings.free_delivery_threshold:
        delivery_fee = settings.delivery_fee
    
    context = {
        'cart': cart,
        'items': items,
        'delivery_fee': delivery_fee,
        'grand_total': cart.total + delivery_fee,
        'free_threshold': settings.free_delivery_threshold,
    }
    return render(request, 'store/cart.html', context)


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    cart = get_or_create_cart(request)
    quantity = int(request.POST.get('quantity', 1))
    
    if not product.is_in_stock:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Product is out of stock'})
        messages.error(request, 'Sorry, this product is out of stock.')
        return redirect('product_detail', slug=product.slug)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'{product.name} added to cart!',
            'cart_count': cart.total_items,
            'cart_total': str(cart.total),
        })
    
    messages.success(request, f'✓ {product.name} added to cart!')
    return redirect('cart')


@require_POST
def remove_from_cart(request, item_id):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(id=item_id, cart=cart).delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'cart_count': cart.total_items, 'cart_total': str(cart.total)})
    
    messages.success(request, 'Item removed from cart.')
    return redirect('cart')


@require_POST
def update_cart(request, item_id):
    cart = get_or_create_cart(request)
    quantity = int(request.POST.get('quantity', 1))
    
    try:
        item = CartItem.objects.get(id=item_id, cart=cart)
        if quantity <= 0:
            item.delete()
        else:
            item.quantity = quantity
            item.save()
        
        return JsonResponse({
            'success': True,
            'subtotal': str(item.subtotal) if quantity > 0 else '0',
            'cart_total': str(cart.total),
            'cart_count': cart.total_items,
        })
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False})


# ─── CHECKOUT ─────────────────────────────────────────────────────────────────────
def checkout(request):
    cart = get_or_create_cart(request)
    if cart.item_count == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('shop')
    
    settings = SiteSettings.get_settings()
    delivery_fee = 0
    if cart.total < settings.free_delivery_threshold:
        delivery_fee = settings.delivery_fee
    
    user_data = {}
    if request.user.is_authenticated:
        user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
    
    if request.method == 'POST':
        # Validate coupon
        coupon_code = request.POST.get('coupon_code', '').strip()
        discount = 0
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code__iexact=coupon_code, is_active=True)
                if coupon.used_count < coupon.usage_limit:
                    if coupon.discount_type == 'percent':
                        discount = cart.total * coupon.discount_value / 100
                    else:
                        discount = coupon.discount_value
                    coupon.used_count += 1
                    coupon.save()
            except Coupon.DoesNotExist:
                pass
        
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            region=request.POST.get('region', ''),
            delivery_notes=request.POST.get('delivery_notes', ''),
            payment_method=request.POST.get('payment_method', 'mpesa'),
            payment_reference=request.POST.get('payment_reference', ''),
            subtotal=cart.total,
            delivery_fee=delivery_fee,
            discount=discount,
            total=cart.total + delivery_fee - discount,
        )
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_name=str(item.product),
                product_price=item.product.price,
                quantity=item.quantity,
                subtotal=item.subtotal,
            )
            if item.product.track_inventory:
                item.product.stock -= item.quantity
                item.product.save(update_fields=['stock'])
        
        cart.items.all().delete()
        
        messages.success(request, f'🎉 Order #{order.order_number} placed successfully!')
        return redirect('order_success', order_number=order.order_number)
    
    context = {
        'cart': cart,
        'delivery_fee': delivery_fee,
        'grand_total': cart.total + delivery_fee,
        'user_data': user_data,
        'settings': settings,
    }
    return render(request, 'store/checkout.html', context)


def order_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'store/order_success.html', {'order': order})


@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})


# ─── WISHLIST ─────────────────────────────────────────────────────────────────────
@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'store/wishlist.html', {'items': items})


@login_required
@require_POST
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    obj, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        obj.delete()
        added = False
    else:
        added = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'added': added})
    
    msg = f'Added {product.name} to wishlist!' if added else f'Removed {product.name} from wishlist.'
    messages.success(request, msg)
    return redirect('product_detail', slug=product.slug)


# ─── SKIN QUIZ ────────────────────────────────────────────────────────────────────
def skin_quiz(request):
    if request.method == 'POST':
        skin_type = request.POST.get('skin_type')
        concerns = ','.join(request.POST.getlist('concerns'))
        routine = request.POST.get('routine')
        
        # AI-powered recommendation logic
        recommendations = get_quiz_recommendations(skin_type, concerns.split(','))
        
        SkinQuiz.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key,
            skin_type=skin_type,
            concerns=concerns,
            routine=routine,
            result=json.dumps([str(p.pk) for p in recommendations]),
        )
        
        context = {
            'skin_type': skin_type,
            'concerns': concerns.split(','),
            'recommendations': recommendations,
        }
        return render(request, 'store/quiz_result.html', context)
    
    return render(request, 'store/skin_quiz.html')


def get_quiz_recommendations(skin_type, concerns):
    products = Product.objects.filter(is_active=True)
    if skin_type and skin_type != 'normal':
        products = products.filter(Q(skin_type=skin_type) | Q(skin_type='all'))
    
    if 'acne' in ' '.join(concerns).lower():
        products = products.filter(Q(name__icontains='acne') | Q(description__icontains='acne') | Q(skin_type='acne_prone'))
    
    return products[:6]


# ─── PROFILE ─────────────────────────────────────────────────────────────────────
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    orders = Order.objects.filter(user=request.user)[:5]
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    context = {
        'orders': orders,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'store/profile.html', context)


# ─── NEWSLETTER ───────────────────────────────────────────────────────────────────
@require_POST
def newsletter_subscribe(request):
    email = request.POST.get('email', '').strip()
    if email:
        Newsletter.objects.get_or_create(email=email)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
        messages.success(request, '🌿 Thank you for subscribing to Pendo Essence!')
    return redirect(request.META.get('HTTP_REFERER', '/'))


# ─── REVIEW ───────────────────────────────────────────────────────────────────────
@login_required
@require_POST
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rating = int(request.POST.get('rating', 5))
    title = request.POST.get('title', '')
    comment = request.POST.get('comment', '')
    
    Review.objects.update_or_create(
        product=product,
        user=request.user,
        defaults={'rating': rating, 'title': title, 'comment': comment, 'is_approved': True}
    )
    messages.success(request, 'Thank you for your review!')
    return redirect('product_detail', slug=product.slug)


# ─── STATIC PAGES ─────────────────────────────────────────────────────────────────
def about(request):
    settings = SiteSettings.get_settings()
    return render(request, 'store/about.html', {'settings': settings})


def contact(request):
    settings = SiteSettings.get_settings()
    if request.method == 'POST':
        messages.success(request, 'Thank you for your message! We will get back to you within 24 hours.')
        return redirect('contact')
    return render(request, 'store/contact.html', {'settings': settings})


def search(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(is_active=True)
    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(brand__icontains=q) | Q(description__icontains=q)
        )
    return render(request, 'store/search.html', {'products': products, 'q': q})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Pendo Essence.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
