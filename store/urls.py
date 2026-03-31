from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search'),
    
    # Cart
    path('cart/', views.cart, name='cart'),
    path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    path('order/success/<str:order_number>/', views.order_success, name='order_success'),
    path('order/<str:order_number>/', views.order_detail, name='order_detail'),
    path('my-orders/', views.my_orders, name='my_orders'),
    
    # Wishlist
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/toggle/<uuid:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    
    # User
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Quiz
    path('skin-quiz/', views.skin_quiz, name='skin_quiz'),
    
    # Other
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('review/<uuid:product_id>/', views.add_review, name='add_review'),
]
