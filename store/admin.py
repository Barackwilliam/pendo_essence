from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .forms import CategoryForm, ProductForm
from .models import (
    Category, Product, ProductImage, Review, Cart, CartItem,
    Order, OrderItem, Wishlist, Newsletter, SkinQuiz, Coupon, SiteSettings
)

UPLOADCARE_PUBLIC_KEY = '4c3ba9de492e0e0eaddc'

# ====================== CATEGORY ADMIN ======================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    
    list_display = ['image_preview', 'name', 'description', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name']
    readonly_fields = ['image_preview']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': UPLOADCARE_PUBLIC_KEY,
                'data-images-only': 'true',
            })
        return formfield

    def image_preview(self, obj):
        url = obj.get_image_preview_url() if obj.image else None
        if url:
            return mark_safe(f'<img src="{url}" style="width:50px;height:50px;object-fit:cover;border-radius:8px;">')
        return '—'
    image_preview.short_description = 'Picha'

    def product_count(self, obj):
        return obj.product_count()   # hii inafanya kazi kwa sababu ni method kwenye model
    product_count.short_description = 'Products'


# ====================== PRODUCT ADMIN ======================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    
    list_display = ['name', 'category', 'price', 'stock_status', 
                    'is_featured', 'is_bestseller', 'is_active']
    list_editable = ['is_featured', 'is_bestseller', 'is_active']
    list_filter = ['category', 'skin_type', 'is_active']
    search_fields = ['name', 'brand']
    readonly_fields = ['views', 'created_at', 'updated_at', 'image_preview', 'image2_preview', 'image3_preview']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ('image', 'image2', 'image3'):
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': UPLOADCARE_PUBLIC_KEY,
                'data-images-only': 'true',
            })
        return formfield

    

    def image_preview(self, obj):
        url = obj.get_image_url() if obj.image else None
        if url:
            return mark_safe(f'<img src="{url}" style="max-height:150px;border-radius:8px;">')
        return '—'
    image_preview.short_description = 'Image 1'

    def image2_preview(self, obj):
        url = obj.get_image2_url() if obj.image2 else None
        if url:
            return mark_safe(f'<img src="{url}" style="max-height:150px;border-radius:8px;">')
        return '—'
    image2_preview.short_description = 'Image 2'

    def image3_preview(self, obj):
        url = obj.get_image3_url() if obj.image3 else None
        if url:
            return mark_safe(f'<img src="{url}" style="max-height:150px;border-radius:8px;">')
        return '—'
    image3_preview.short_description = 'Image 3'

    def stock_status(self, obj):
        if obj.stock <= 0:
            return mark_safe('<span style="color:red;font-weight:bold;">Out of Stock</span>')
        elif obj.is_low_stock:
            return mark_safe(f'<span style="color:orange;font-weight:bold;">Low ({obj.stock})</span>')
        return mark_safe(f'<span style="color:green;">In Stock ({obj.stock})</span>')
    stock_status.short_description = 'Stock'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'product_price', 'quantity', 'subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'city', 'total_display',
                    'payment_method', 'is_paid', 'status', 'created_at']
    list_filter = ['status', 'payment_method', 'is_paid', 'city']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_editable = ['status', 'is_paid']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    inlines = [OrderItemInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Customer'

    def total_display(self, obj):
        return format_html('<strong>TZS {:,}</strong>', int(obj.total))
    total_display.short_description = 'Total'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'title', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['rating', 'is_approved']
    search_fields = ['product__name', 'user__username', 'comment']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'created_at']
    list_filter = ['is_active']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'discount_value', 'used_count', 'usage_limit', 'is_active', 'expires_at']
    list_editable = ['is_active']


admin.site.register(Wishlist)
admin.site.register(SkinQuiz)
