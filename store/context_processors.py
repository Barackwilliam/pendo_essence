from .models import SiteSettings, Category


def cart_processor(request):
    from .views import get_or_create_cart
    try:
        cart = get_or_create_cart(request)
        return {
            'cart': cart,
            'cart_count': cart.total_items,
        }
    except Exception:
        return {'cart': None, 'cart_count': 0}


def site_settings_processor(request):
    return {
        'site_settings': SiteSettings.get_settings(),
        'nav_categories': Category.objects.filter(is_active=True)[:8],
    }
