"""
Pendo Essence - Populate Sample Data
Run: python manage.py shell < populate_data.py
OR:  python manage.py runscript populate_data  (if django-extensions installed)
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pendo_essence.settings')
django.setup()

from store.models import Category, Product, SiteSettings

# ── Site Settings ──────────────────────────────────────────
settings, _ = SiteSettings.objects.get_or_create(pk=1)
settings.site_name = "Pendo Essence"
settings.tagline = "Stay Natural, Stay Beautiful"
settings.phone = "+255 712 345 678"
settings.whatsapp = "712345678"
settings.email = "info@pendoessence.co.tz"
settings.address = "Dar es Salaam, Tanzania"
settings.instagram = "https://instagram.com/pendo_essence"
settings.facebook = "https://facebook.com/pendoessence"
settings.tiktok = "https://tiktok.com/@pendo_essence"
settings.free_delivery_threshold = 50000
settings.delivery_fee = 5000
settings.save()
print("✓ Site settings configured")

# ── Categories ─────────────────────────────────────────────
categories_data = [
    {"name": "Facial Cleansers", "icon": "fa-soap", "desc": "Gentle cleansers for African skin", "order": 1},
    {"name": "Toners", "icon": "fa-tint", "desc": "Balance and prep your skin", "order": 2},
    {"name": "Moisturisers", "icon": "fa-droplet", "desc": "Deep hydration for all skin types", "order": 3},
    {"name": "Serums", "icon": "fa-flask", "desc": "Targeted treatments for specific concerns", "order": 4},
    {"name": "Deodorants", "icon": "fa-wind", "desc": "Natural deodorant solutions", "order": 5},
    {"name": "Hair Removal", "icon": "fa-magic", "desc": "Smooth skin solutions", "order": 6},
    {"name": "Feminine Care", "icon": "fa-heart", "desc": "Gentle feminine hygiene products", "order": 7},
    {"name": "Virgin Coconut Oil", "icon": "fa-seedling", "desc": "Pure natural coconut oil", "order": 8},
]

cats = {}
for cd in categories_data:
    from django.utils.text import slugify
    cat, _ = Category.objects.get_or_create(
        name=cd["name"],
        defaults={"icon": cd["icon"], "description": cd["desc"], "order": cd["order"], "slug": slugify(cd["name"])}
    )
    cats[cd["name"]] = cat
    print(f"✓ Category: {cat.name}")

# ── Products ───────────────────────────────────────────────
products_data = [
    # Facial Cleansers
    {"name": "PanOxyl Acne Foaming Wash 10% Benzoyl Peroxide", "category": "Facial Cleansers",
     "price": 32000, "compare_price": 38000, "size": "156g", "stock": 20,
     "skin_type": "acne_prone", "is_featured": True,
     "short_description": "Maximum strength 10% benzoyl peroxide acne wash for body and face.",
     "description": "PanOxyl Acne Foaming Wash 10% Benzoyl Peroxide is a dermatologist recommended maximum strength acne foaming wash. It kills acne-causing bacteria and helps prevent new breakouts. Safe for use on face, chest, and back.",
     "benefits": "Kills acne-causing bacteria\nPrevents new breakouts\nClears blackheads and whiteheads\nDermatologist recommended\nSafe for body and face",
     "brand": "PanOxyl"},
    
    {"name": "CeraVe SA Smoothing Cleanser", "category": "Facial Cleansers",
     "price": 28000, "compare_price": None, "size": "236g", "stock": 15,
     "skin_type": "dry", "is_new_arrival": True,
     "short_description": "Exfoliating cleanser with salicylic acid for rough, bumpy skin.",
     "description": "CeraVe SA Smoothing Cleanser gently exfoliates, smooths skin texture, and helps retain skin moisture. Contains 3 essential ceramides and salicylic acid.",
     "benefits": "Gently exfoliates\nSmooths rough texture\nRetains moisture\nContains essential ceramides",
     "brand": "CeraVe"},
    
    {"name": "CeraVe Foaming Cleanser", "category": "Facial Cleansers",
     "price": 26000, "compare_price": None, "size": "236g", "stock": 18,
     "skin_type": "oily",
     "short_description": "Foaming face wash for normal to oily skin with essential ceramides.",
     "description": "CeraVe Foaming Facial Cleanser is developed with dermatologists for daily face washing. It removes oil and cleanses skin without disrupting the skin's natural barrier.",
     "benefits": "Removes excess oil\nCleansing without stripping\n3 essential ceramides\nDermatologist recommended",
     "brand": "CeraVe"},
    
    {"name": "Low pH Good Morning Gel Cleanser", "category": "Facial Cleansers",
     "price": 24000, "compare_price": 28000, "size": "150ml", "stock": 12,
     "skin_type": "combination", "is_bestseller": True,
     "short_description": "Gentle pH-balanced morning cleanser for healthy skin barrier.",
     "description": "COSRX Low pH Good Morning Gel Cleanser maintains skin pH balance with natural BHA from willow bark water. Perfect for daily morning use.",
     "benefits": "Maintains pH balance\nNatural BHA exfoliant\nNon-stripping formula\nSuitable for all skin types",
     "brand": "COSRX"},

    {"name": "Neutrogena Oil Balancing Cleanser", "category": "Facial Cleansers",
     "price": 22000, "compare_price": None, "size": "200ml", "stock": 22,
     "skin_type": "oily",
     "short_description": "Controls shine and excess oil without over-drying.",
     "description": "Neutrogena Oil Balancing Cleanser effectively removes excess oil and impurities while maintaining natural moisture balance.",
     "benefits": "Controls excess oil\nMaintains natural balance\nNon-comedogenic\nRefreshing formula",
     "brand": "Neutrogena"},

    # Toners
    {"name": "The Ordinary Glycolic Acid 7% Exfoliating Toner", "category": "Toners",
     "price": 19000, "compare_price": None, "size": "100ml", "stock": 25,
     "skin_type": "combination", "is_featured": True, "is_natural": False,
     "short_description": "High-strength glycolic acid toner for improved skin texture and tone.",
     "description": "This weekly glycolic acid toning solution improves skin texture, brightness, and clarity. A cult-favorite for achieving glowing, even skin.",
     "benefits": "Improves skin texture\nBrightens dull skin\nEvens skin tone\nReduces dark spots\nExfoliates gently",
     "brand": "The Ordinary"},

    # Moisturisers
    {"name": "Dr. Althea 345 Relief Cream", "category": "Moisturisers",
     "price": 38000, "compare_price": 46000, "size": "50ml", "stock": 10,
     "skin_type": "sensitive", "is_featured": True, "is_bestseller": True,
     "short_description": "Soothing barrier cream with 345 calming ingredients for sensitive skin.",
     "description": "Dr. Althea 345 Relief Cream is formulated with 345 skin-soothing ingredients to calm irritated and sensitive skin while repairing the skin barrier.",
     "benefits": "Soothes irritated skin\nRepairs skin barrier\n345 calming ingredients\nLong-lasting hydration",
     "brand": "Dr. Althea"},
    
    {"name": "The Ordinary Natural Moisturizing Factor + HA", "category": "Moisturisers",
     "price": 18000, "compare_price": None, "size": "30ml", "stock": 30,
     "skin_type": "all", "is_new_arrival": True,
     "short_description": "Surface moisturizer with amino acids and hyaluronic acid.",
     "description": "An in-depth formula that combines NMF components and hyaluronic acid for immediate and sustained surface hydration.",
     "benefits": "Immediate hydration\nHyaluronic acid complex\nNon-greasy finish\nSuitable for all skin types",
     "brand": "The Ordinary"},

    {"name": "Oh So Heavenly Dark Spot Corrector", "category": "Moisturisers",
     "price": 22000, "compare_price": 28000, "size": "30ml", "stock": 14,
     "skin_type": "all", "is_featured": True,
     "short_description": "Targeted treatment for dark spots and uneven skin tone.",
     "description": "Oh So Heavenly Dark Spot Corrector helps visibly reduce the appearance of dark spots, hyperpigmentation, and uneven skin tone.",
     "benefits": "Reduces dark spots\nEvens skin tone\nReduces hyperpigmentation\nSuitable for African skin",
     "brand": "Oh So Heavenly"},

    {"name": "NIVEA Vitamin E Day Cream Moisturiser", "category": "Moisturisers",
     "price": 16000, "compare_price": None, "size": "50ml", "stock": 35,
     "skin_type": "normal",
     "short_description": "Daily moisturizer with Vitamin E for nourished, radiant skin.",
     "description": "NIVEA Vitamin E Day Cream moisturizes and protects skin with antioxidant Vitamin E for visibly healthier skin.",
     "benefits": "Daily protection\nVitamin E antioxidant\nNourishes skin\nRadiant complexion",
     "brand": "NIVEA"},

    # Deodorants
    {"name": "Mitchum Women Unscented Deodorant", "category": "Deodorants",
     "price": 18000, "compare_price": None, "size": "63g", "stock": 20,
     "skin_type": "sensitive",
     "short_description": "48-hour odor protection, unscented for sensitive skin.",
     "description": "Mitchum Women Unscented provides 48-hour protection with no perfume for sensitive skin. Dermatologist tested.",
     "benefits": "48-hour protection\nUnscented formula\nSensitive skin friendly\nDermatologist tested",
     "brand": "Mitchum"},

    # Virgin Coconut Oil
    {"name": "Virgin Coconut Oil", "category": "Virgin Coconut Oil",
     "price": 12000, "compare_price": None, "size": "100ml", "stock": 50,
     "skin_type": "all", "is_featured": True, "is_bestseller": True, "is_new_arrival": True,
     "short_description": "Pure, cold-pressed virgin coconut oil for skin and hair.",
     "description": "Our premium Virgin Coconut Oil is cold-pressed from fresh coconuts to retain maximum nutrients. Perfect for moisturizing African skin, hair treatment, and natural beauty routines.",
     "benefits": "Deep moisturization\nNatural hair conditioner\nAnti-bacterial properties\nRich in antioxidants\nVersatile beauty oil",
     "brand": "Pendo Essence"},

    {"name": "Virgin Coconut Oil", "category": "Virgin Coconut Oil",
     "price": 16000, "compare_price": None, "size": "150ml", "stock": 45,
     "skin_type": "all", "is_featured": True, "is_bestseller": True,
     "short_description": "Premium cold-pressed virgin coconut oil — larger size.",
     "description": "Our premium Virgin Coconut Oil is cold-pressed from fresh coconuts to retain maximum nutrients. Larger size for your complete skincare and hair routine.",
     "benefits": "Deep moisturization\nNatural hair conditioner\nAnti-bacterial properties\nRich in antioxidants",
     "brand": "Pendo Essence"},
]

for pd in products_data:
    from django.utils.text import slugify
    category = cats.get(pd["category"])
    slug_base = slugify(f"{pd['name']}-{pd['size']}")
    
    product, created = Product.objects.get_or_create(
        slug=slug_base,
        defaults={
            "name": pd["name"],
            "category": category,
            "price": pd["price"],
            "compare_price": pd.get("compare_price"),
            "size": pd["size"],
            "stock": pd["stock"],
            "skin_type": pd.get("skin_type", "all"),
            "is_featured": pd.get("is_featured", False),
            "is_bestseller": pd.get("is_bestseller", False),
            "is_new_arrival": pd.get("is_new_arrival", False),
            "is_natural": pd.get("is_natural", True),
            "short_description": pd.get("short_description", ""),
            "description": pd.get("description", ""),
            "benefits": pd.get("benefits", ""),
            "brand": pd.get("brand", ""),
        }
    )
    status = "Created" if created else "Exists"
    print(f"✓ {status}: {product.name} ({product.size})")

print("\n🎉 Sample data populated successfully!")
print(f"   Categories: {Category.objects.count()}")
print(f"   Products: {Product.objects.count()}")
print("\n👤 Create admin user:")
print("   python manage.py createsuperuser")
