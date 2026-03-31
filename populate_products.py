
from store.models import Category, Product

print("🌿 Starting to load categories and products...")

# ─────────────────────────────────────────────────────────────────────────────
# CATEGORIES
# ─────────────────────────────────────────────────────────────────────────────

categories_data = [
    {
        'name': 'Facial Cleansers',
        'slug': 'facial-cleansers',
        'description': 'Cleanse your face gently and effectively. Our facial cleansers remove dirt, excess oil and makeup without harming your skin. Suitable for all skin types.',
        'icon': 'fa-face-smile',
        'order': 1,
    },
    {
        'name': 'Toners',
        'slug': 'toners',
        'description': 'Balance your skin and maintain proper pH levels. Our toners open pores, remove remaining impurities and prepare your skin to absorb moisturizer and serum more effectively.',
        'icon': 'fa-droplet',
        'order': 2,
    },
    {
        'name': 'Moisturisers',
        'slug': 'moisturisers',
        'description': 'Nourish and protect your skin every day. Our moisturisers contain high-quality ingredients that soften, hydrate and shield skin against harsh weather conditions and premature aging.',
        'icon': 'fa-jar',
        'order': 3,
    },
    {
        'name': 'Deodorants',
        'slug': 'deodorants',
        'description': 'Stay fresh and confident all day. Our deodorants ensure you breathe freely, prevent bad odor and make you feel fully confident at all times.',
        'icon': 'fa-wind',
        'order': 4,
    },
    {
        'name': 'Hair Removal',
        'slug': 'hair-removal',
        'description': 'The best hair removal products without pain. From smooth creams to shaving oils, we give you smooth and clean skin that lasts longer.',
        'icon': 'fa-spa',
        'order': 5,
    },
    {
        'name': 'Feminine Wash',
        'slug': 'feminine-wash',
        'description': 'Intimate area hygiene with gentleness and safety. Our feminine wash products have the correct pH balance, are extremely gentle and protect you against infections.',
        'icon': 'fa-heart',
        'order': 6,
    },
    {
        'name': 'Accessories',
        'slug': 'accessories',
        'description': 'Essential skincare tools. Cotton pads, applicators and other tools to help us achieve the best results from our products.',
        'icon': 'fa-stars',
        'order': 7,
    },
]

cats = {}
for c in categories_data:
    obj, created = Category.objects.update_or_create(
        slug=c['slug'],
        defaults={
            'name': c['name'],
            'description': c['description'],
            'icon': c['icon'],
            'order': c['order'],
            'is_active': True,
            'image': '', 
        }
    )
    cats[c['slug']] = obj
    print(f"  {'✅ Created' if created else '🔄 Updated'}: {obj.name}")

print("\n🛍️  Starting to load products...\n")

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCTS
# ─────────────────────────────────────────────────────────────────────────────

products_data = [

    # ══════════════════════════════════════════════════════════════
    # FACIAL CLEANSERS
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'facial-cleansers',
        'name': 'PanOxyl Acne Foaming Wash 10% Benzoyl Peroxide',
        'brand': 'PanOxyl',
        'size': '156g',
        'skin_type': 'acne_prone',
        'price': 32000,
        'compare_price': 38000,
        'stock': 30,
        'is_featured': True,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'The best acne treatment — 10% Benzoyl Peroxide kills acne bacteria powerfully and quickly.',
        'description': (
            'PanOxyl Acne Foaming Wash is a powerful cleanser designed specifically for acne-prone skin. '
            'It contains Benzoyl Peroxide 10% — the highest concentration available without a prescription — '
            'which penetrates deep into pores and kills *Cutibacterium acnes* (P. acnes) bacteria before it causes inflammation. '
            'Its gentle foaming formula cleanses deeply without leaving skin dry or irritated. '
            'Particularly effective for people with severe acne, deep (cystic) acne and red inflammatory acne. '
            'Dermatologists strongly recommend it as the first step in acne treatment.'
        ),
        'ingredients': 'Benzoyl Peroxide 10%, Purified Water, Sodium Lauroamphoacetate, Sodium C14-16 Olefin Sulfonate, Sodium Methyl Cocoyl Taurate, Sodium Hydroxide, Propylene Glycol, Sodium Hyaluronate.',
        'how_to_use': 'Wet your face with lukewarm water. Place a small amount of PanOxyl on your palm and lather up. Gently massage onto face for 30-60 seconds. Rinse thoroughly with cold water. Use once or twice daily. Follow with an SPF moisturizer in the morning.',
        'benefits': 'Kills acne bacteria (P. acnes) quickly\nReduces new acne breakouts\nUnclogs blocked pores\nWorks from the very first use\nRecommended by dermatologists',
        'meta_title': 'PanOxyl Acne Foaming Wash 10% Benzoyl Peroxide 156g | Pendo Essence',
        'meta_description': 'The best acne treatment. PanOxyl Acne Foaming Wash has 10% Benzoyl Peroxide that kills acne bacteria and reduces inflammation. Buy online Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'CeraVe SA Smoothing Cleanser',
        'brand': 'CeraVe',
        'size': '236g',
        'skin_type': 'dry',
        'price': 28000,
        'compare_price': 34000,
        'stock': 25,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Exfoliate and moisturize at once — Salicylic Acid + Ceramides for smooth and vibrant skin.',
        'description': (
            'CeraVe SA Smoothing Cleanser is a unique cleanser that combines the power of exfoliation and moisture protection. '
            'Its Salicylic Acid removes dead skin cells, unclogs pores and smooths skin texture. '
            'Meanwhile, Ceramides 1, 3 and 6-II rebuild the skin barrier, '
            'ensuring your skin does not lose too much moisture after cleansing. '
            'Formulated with CeraVe\'s unique MVE Technology that releases moisture slowly over 24 hours. '
            'Suitable for dry skin, skin with small bumps (keratosis pilaris) and skin that feels rough or unsmoothed.'
        ),
        'ingredients': 'Salicylic Acid 0.5%, Ceramide NP, Ceramide AP, Ceramide EOP, Hyaluronic Acid, Niacinamide, Phytosphingosine, Cholesterol, Sodium Lauroyl Sarcosinate.',
        'how_to_use': 'Apply a small amount to your wet hands. Massage in circular motions on dampened face. Rinse well with normal temperature water. Pat dry with a soft towel. Use morning and evening.',
        'benefits': 'Smooths rough, uneven skin\nRemoves dead skin cells\nRetains skin moisture\nRebuilds skin barrier\nDoes not irritate sensitive skin',
        'meta_title': 'CeraVe SA Smoothing Cleanser 236g | Pendo Essence Tanzania',
        'meta_description': 'CeraVe SA Smoothing Cleanser with Salicylic Acid and Ceramides that smooths, exfoliates and protects dry skin. Buy Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'CeraVe Foaming Cleanser',
        'brand': 'CeraVe',
        'size': '236g',
        'skin_type': 'oily',
        'price': 26000,
        'compare_price': 32000,
        'stock': 40,
        'is_featured': False,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'Cleanse deeply, retain moisture — Ceramides and Hyaluronic Acid for oily skin.',
        'description': (
            'CeraVe Foaming Cleanser is a globally loved cleanser for oily and normal skin types. '
            'Its rich foam cleanses deeply, removing excess oil, dirt and makeup while avoiding drying out the skin. '
            'Formulated with three essential Ceramides (1, 3 and 6-II) that protect and rebuild your natural skin barrier. '
            'Added Hyaluronic Acid ensures skin retains the moisture it needs. '
            'Non-comedogenic (does not clog pores), fragrance-free and tested for sensitive skin. '
            'Developed in collaboration with dermatologists and recommended by over 90% of dermatologists in the USA.'
        ),
        'ingredients': 'Ceramide NP, Ceramide AP, Ceramide EOP, Hyaluronic Acid, Niacinamide, Sodium Lauroyl Sarcosinate, PEG-21 Stearyl Ether Sulfate.',
        'how_to_use': 'Wet face with water. Put a small amount on palms, lather and gently massage onto face and neck for 30 seconds. Rinse thoroughly. Pat dry with a soft towel without rubbing. Follow with a moisturizer.',
        'benefits': 'Removes excess oil without drying\nPreserves skin\'s natural ceramides\nEvens out skin tone\nDoes not clog pores\nSuitable for sensitive skin',
        'meta_title': 'CeraVe Foaming Cleanser 236g for Oily Skin | Pendo Essence',
        'meta_description': 'CeraVe Foaming Cleanser with Ceramides and Hyaluronic Acid cleanses deeply without drying. Best for oily skin. Buy Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'CeraVe Blemish Control Cleanser',
        'brand': 'CeraVe',
        'size': '236g',
        'skin_type': 'acne_prone',
        'price': 28000,
        'compare_price': 35000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Fight acne while protecting skin — 2% Salicylic Acid and Ceramides in one formula.',
        'description': (
            'CeraVe Blemish Control Cleanser is the complete answer for those struggling with acne who still want to protect their skin. '
            'It contains 2% Salicylic Acid that penetrates deep into pores, controlling excess oil and removing dead skin cells '
            'which are the primary cause of acne. Unlike many acne cleansers that over-dry, '
            'CeraVe has added Ceramides and Niacinamide that protect and shield the skin. '
            'Niacinamide also helps reduce dark spots (post-acne marks) that remain after breakouts. '
            'This gentle formula is suitable even for sensitive acne-prone skin.'
        ),
        'ingredients': 'Salicylic Acid 2%, Ceramide NP, Ceramide AP, Ceramide EOP, Niacinamide, Zinc PCA, Hyaluronic Acid, Panthenol.',
        'how_to_use': 'Use morning and/or evening. Apply a sufficient amount to your hands, lather, massage onto wet face for 60 seconds. Rinse well with cold water. Follow with toner or moisturizer.',
        'benefits': 'Fights acne with 2% Salicylic Acid\nUnclogs blocked pores\nReduces post-acne dark spots\nProtects skin with Ceramides\nDoes not over-dry skin',
        'meta_title': 'CeraVe Blemish Control Cleanser 236g | Acne | Pendo Essence',
        'meta_description': 'CeraVe Blemish Control Cleanser has 2% Salicylic Acid and Ceramides fighting acne while protecting skin. Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'COSRX Low pH Good Morning Gel Cleanser',
        'brand': 'COSRX',
        'size': '150ml',
        'skin_type': 'combination',
        'price': 30000,
        'compare_price': 36000,
        'stock': 18,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'A low pH morning cleanser — cleanses gently while maintaining your skin\'s natural balance.',
        'description': (
            'COSRX Low pH Good Morning Gel Cleanser is one of the most popular K-beauty cleansers worldwide, and for good reason. '
            'Formulated at a pH of 5.0 — close to the skin\'s natural pH (4.5–5.5) — ensuring skin does not lose its balance. '
            'Many cleansers have a high pH (7-9) that disrupts the skin barrier and causes oiliness, dryness, or irritation. '
            'Low pH Good Morning Gel cleanses gently, removes overnight oil and leaves skin ready to receive subsequent products. '
            'Its Tea Tree Oil has antibacterial properties, helping to prevent acne. '
            'Particularly great for those following a K-beauty routine or wanting a light morning cleanser.'
        ),
        'ingredients': 'Saccharomyces Ferment Filtrate, Butylene Glycol, BHA (Betaine Salicylate 0.5%), Tea Tree Oil, Allantoin, Panthenol, Hyaluronic Acid.',
        'how_to_use': 'Wet face with cold water. Apply a small amount of gel to palms and lather. Gently massage onto face for 30 seconds. Rinse thoroughly with cold water. Follow with a low pH toner.',
        'benefits': 'Maintains skin\'s natural pH\nCleanses gently without stripping moisture\nInhibits growth of acne bacteria\nLeaves skin smooth and clean\nSuitable for K-beauty routine',
        'meta_title': 'COSRX Low pH Good Morning Gel Cleanser 150ml | Pendo Essence',
        'meta_description': 'COSRX Low pH Good Morning Gel Cleanser cleanses gently at the right pH for better skin. Best K-beauty Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'Neutrogena Oil Balancing Cleanser',
        'brand': 'Neutrogena',
        'size': '200ml',
        'skin_type': 'oily',
        'price': 22000,
        'compare_price': 27000,
        'stock': 35,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Balance skin oil without drying it out — a dermatologist-tested formula for a shine-free complexion.',
        'description': (
            'Neutrogena Oil Balancing Cleanser is designed specifically for oily skin. '
            'Its unique formula works in two ways: it cleanses away excess oil that damages the face '
            'while simultaneously controlling sebum production over a longer period. '
            'This means your face stays clean and matte much longer than with regular cleansers. '
            'Particularly great for those troubled by a shiny face (oily sheen) during the day hours after cleansing. '
            'Dermatologist-tested, hypoallergenic and does not dry out skin.'
        ),
        'ingredients': 'Salicylic Acid, Witch Hazel Extract, Glycerin, Cocamidopropyl Betaine, PEG-80 Sorbitan Laurate, Fragrance.',
        'how_to_use': 'Wet face with warm water. Apply a small amount to palms and lather. Massage in circular motions onto face for 60 seconds. Rinse thoroughly. Use twice daily for best results.',
        'benefits': 'Controls excess oil\nKeeps skin matte for longer\nCleanses pores\nDermatologist-verified\nDoes not irritate skin',
        'meta_title': 'Neutrogena Oil Balancing Cleanser 200ml | Pendo Essence Tanzania',
        'meta_description': 'Neutrogena Oil Balancing Cleanser balances skin oil without drying it out. Best for oily skin. Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'Neutrogena Spot Controlling Cleanser',
        'brand': 'Neutrogena',
        'size': '200ml',
        'skin_type': 'acne_prone',
        'price': 22000,
        'compare_price': 27000,
        'stock': 28,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Target acne directly — a specialized formula that fights acne and dark spots.',
        'description': (
            'Neutrogena Spot Controlling Cleanser is the first step in the fight against acne. '
            'Its enhanced formula targets acne-prone areas directly, helping to reduce inflammation '
            'and redness quickly. The added Salicylic Acid works inside the pore, clearing the dirt '
            'and oil that causes acne. Particularly suitable for teenage skin and people who suffer from '
            'frequent breakouts. Does not irritate skin and can be used alongside other acne treatments.'
        ),
        'ingredients': 'Salicylic Acid 2%, Glycerin, Aloe Vera, Zinc PCA, PEG-80 Sorbitan Laurate, Cocamidopropyl Betaine.',
        'how_to_use': 'Wet face with water. Apply a small amount to palms, lather and gently massage for 60 seconds, focusing on acne-prone areas. Rinse thoroughly. Use twice daily.',
        'benefits': 'Targets acne directly\nReduces inflammation and redness\nWorks quickly\nPrevents new breakouts\nSuitable for teenage skin',
        'meta_title': 'Neutrogena Spot Controlling Cleanser 200ml | Acne | Pendo Essence',
        'meta_description': 'Neutrogena Spot Controlling Cleanser targets acne directly and reduces inflammation. Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'Neutrogena Refreshingly Clear Cleanser',
        'brand': 'Neutrogena',
        'size': '200ml',
        'skin_type': 'combination',
        'price': 22000,
        'compare_price': 27000,
        'stock': 30,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Feel freshness instantly — a daily cleanser that cleanses and refreshes your skin.',
        'description': (
            'Neutrogena Refreshingly Clear Daily Cleanser brings a feeling of true freshness and cleanliness every morning and evening. '
            'Designed for normal to combination skin, it cleanses gently '
            'while leaving a refreshing and clean feeling. '
            'Its light formula is suitable for daily use, even for sensitive skin. '
            'It helps control oil in the T-zone (forehead, nose, chin) while avoiding drying out the cheeks. '
            'It is a fragrance-rinse-clean formula that removes scent quickly after rinsing.'
        ),
        'ingredients': 'Salicylic Acid, Aloe Vera, Glycerin, Menthol, Cocamidopropyl Betaine, Sodium Laureth Sulfate.',
        'how_to_use': 'Apply a small amount to your palms, add a little water and lather. Gently massage onto wet face for 30-60 seconds. Rinse well and feel the immediate refreshing sensation.',
        'benefits': 'Brings a feeling of freshness and cleanliness\nBalances combination skin\nSuitable for daily use\nKeeps skin clean for longer\nLight and suitable for sensitive skin',
        'meta_title': 'Neutrogena Refreshingly Clear Cleanser 200ml | Pendo Essence',
        'meta_description': 'Neutrogena Refreshingly Clear Cleanser brings a feeling of true freshness and cleanliness to your skin. Tanzania.',
    },
    {
        'category_slug': 'facial-cleansers',
        'name': 'COSRX Salicylic Acid Daily Gentle Cleanser',
        'brand': 'COSRX',
        'size': '150ml',
        'skin_type': 'acne_prone',
        'price': 32000,
        'compare_price': 38000,
        'stock': 22,
        'is_featured': True,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'K-beauty for acne — gentle daily Salicylic Acid that cleanses deeply without irritating.',
        'description': (
            'COSRX Salicylic Acid Daily Gentle Cleanser is the most popular K-beauty cleanser for good reason. '
            'It contains Salicylic Acid well incorporated at a low pH (5.5), meaning it works more effectively than '
            'many SA cleansers that have a pH too high. '
            'It cleanses deeply every day — removing sebum, dirt and dead skin cells — without irritating or drying skin. '
            'Unlike harsh cleansers, this can be used twice daily without leaving your skin sensitive or dry. '
            'Its natural Willow Bark Extract adds antibacterial power. '
            'If you\'re a K-beauty skincare fan, this is a must in your routine.'
        ),
        'ingredients': 'Salicylic Acid, Salix Alba (Willow) Bark Water, Butylene Glycol, Sodium Chloride, Allantoin, Panthenol, Betaine Salicylate.',
        'how_to_use': 'Use twice daily, morning and evening. Wet face with cold water. Apply a small amount of gel to hands, lather gently and massage for 60 seconds. Rinse well with cold water. Follow with toner.',
        'benefits': 'Deeply cleanses pores\nRemoves sebum and dead skin cells\nWorks at the correct pH\nCan be used every day\nPrevents new acne from forming',
        'meta_title': 'COSRX Salicylic Acid Daily Gentle Cleanser 150ml | Pendo Essence',
        'meta_description': 'COSRX Salicylic Acid Daily Gentle Cleanser - the best K-beauty cleanser for acne. Cleanses deeply without irritating. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # TONERS
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'toners',
        'name': 'The Ordinary Glycolic Acid 7% Toning Solution',
        'brand': 'The Ordinary',
        'size': '100ml',
        'skin_type': 'combination',
        'price': 24000,
        'compare_price': 30000,
        'stock': 35,
        'is_featured': True,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'Exfoliate powerfully — 7% Glycolic Acid makes skin smooth, clean and glowing.',
        'description': (
            'The Ordinary Glycolic Acid 7% Toning Solution is a powerful exfoliant toner from the globally loved brand. '
            'Glycolic Acid is an AHA (Alpha Hydroxy Acid) that works most effectively among all AHAs — '
            'its small molecules allow it to penetrate deep into skin, breaking the bonds of dead skin cells '
            'and making them shed painlessly. '
            'Regular use shows improvements in: skin texture (becomes smoother), '
            'skin tone (becomes more even), radiance (a noticeably visible glow) and reduction of fine lines. '
            'Also helps reduce the appearance of pores and dark spots. '
            'Added Amino Acids, Aloe Vera and Ginseng nourish and protect skin.'
        ),
        'ingredients': 'Glycolic Acid 7%, Aqua, Rosa Damascena Flower Water, Aloe Barbadensis Leaf Water, Glycerin, Panax Ginseng Root Extract, Tasmannia Lanceolata Fruit Extract, Amino Acids.',
        'how_to_use': 'Use at night only (Glycolic Acid makes skin more sun-sensitive). Apply a small amount with a cotton swab or hands onto face, neck and décolleté after cleanser. Do not rinse off. Follow with moisturizer. Always wear SPF in the morning.',
        'benefits': 'Removes dead skin cells deeply\nMakes skin texture smoother\nImproves skin radiance\nReduces appearance of spots and fine lines\nMakes pores appear smaller',
        'meta_title': 'The Ordinary Glycolic Acid 7% Toning Solution 100ml | Pendo Essence',
        'meta_description': 'The Ordinary Glycolic Acid 7% Toning Solution makes skin smooth, clean and glowing. Best exfoliant Tanzania.',
    },
    {
        'category_slug': 'toners',
        'name': 'The Ordinary Glycolic Acid 7% Toning Solution',
        'brand': 'The Ordinary',
        'size': '240ml',
        'skin_type': 'combination',
        'price': 42000,
        'compare_price': 52000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Premium value — large bottle of Glycolic Acid 7% for long-term use.',
        'description': (
            'This is the large 240ml bottle of The Ordinary Glycolic Acid 7% Toning Solution — '
            'equivalent to two products at a discounted price. '
            'The formula is the same powerful and effective one: 7% Glycolic Acid that deeply exfoliates, '
            'making skin smoother, more radiant and even-toned. '
            'For those who already love this toner and want to make sure they never run out of stock, '
            'this is the best choice. '
            'Saves money in the long run and ensures you have enough supply for several months of a consistent skincare routine.'
        ),
        'ingredients': 'Glycolic Acid 7%, Aqua, Rosa Damascena Flower Water, Aloe Barbadensis Leaf Water, Glycerin, Panax Ginseng Root Extract, Tasmannia Lanceolata Fruit Extract, Amino Acids.',
        'how_to_use': 'Use at night only. Apply a small amount with cotton or hands onto clean face. Do not rinse. Follow with moisturizer. Always wear SPF in the morning.',
        'benefits': 'Best value (240ml)\nSame powerful formula\nSaves money in the long run\nNo need to buy frequently\nGreat for daily users',
        'meta_title': 'The Ordinary Glycolic Acid 7% 240ml Value Size | Pendo Essence',
        'meta_description': 'The Ordinary Glycolic Acid 7% Toning Solution 240ml - large bottle of great value. Best exfoliant at a great price. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # MOISTURISERS
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'moisturisers',
        'name': 'Dr. Althea 345 Relief Cream',
        'brand': 'Dr. Althea',
        'size': '50ml',
        'skin_type': 'sensitive',
        'price': 45000,
        'compare_price': 55000,
        'stock': 15,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Calm irritated skin — a science-based K-beauty cream for sensitive and reactive skin.',
        'description': (
            'Dr. Althea 345 Relief Cream is designed for skin that is frequently troubled — with redness, itching, '
            'burning or reacting badly to many products. '
            '"345" represents three key ingredients with three different strengths: '
            'Centella Asiatica (soothing), Hyaluronic Acid (hydrating) and Ceramides (protecting). '
            'Centella Asiatica — also known as "tiger grass" or "cica" — has been used for centuries '
            'in Asian medicine to soothe and heal skin. '
            'This cream is particularly great after skin treatments (laser, peel, microneedling), '
            'for skin with mild eczema, or during weather changes that aggravate the skin.'
        ),
        'ingredients': 'Centella Asiatica Extract 40%, Hyaluronic Acid, Ceramide NP, Panthenol, Madecassoside, Asiaticoside, Allantoin, Niacinamide.',
        'how_to_use': 'After cleanser and toner, place a small amount of cream on fingertips and gently massage in circular motions onto face and neck until well absorbed. Use morning and evening. Can be used as a night mask in a thicker layer.',
        'benefits': 'Calms irritated and itchy skin\nReduces redness and inflammation\nRebuilds skin barrier\nDeep hydration\nSuitable after skin treatments',
        'meta_title': 'Dr. Althea 345 Relief Cream 50ml | Sensitive Skin | Pendo Essence',
        'meta_description': 'Dr. Althea 345 Relief Cream with Centella Asiatica soothes sensitive, red and irritated skin. K-beauty Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'Dr. Althea 147 Barrier Cream',
        'brand': 'Dr. Althea',
        'size': '50ml',
        'skin_type': 'dry',
        'price': 45000,
        'compare_price': 55000,
        'stock': 15,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Rebuild your skin barrier — a powerful cream that protects and deeply moisturizes very dry skin.',
        'description': (
            'Dr. Althea 147 Barrier Cream is designed to restore and strengthen a weakened skin barrier. '
            '"147" represents three key strengths: moisturizing, barrier-repair and soothing. '
            'Skin with a weak barrier loses moisture quickly, becomes irritated, and can be affected by external elements. '
            'This cream prevents moisture loss (TEWL - Trans-Epidermal Water Loss) by creating a protective layer '
            'over the skin, while still allowing the skin to breathe. '
            'Particularly great in winter, after long-term use of retinol or AHAs, '
            'or for anyone whose skin feels tight and extremely dry.'
        ),
        'ingredients': 'Ceramide NP 1%, Ceramide AP, Ceramide EOP, Cholesterol, Hyaluronic Acid, Shea Butter, Squalane, Glycerin, Niacinamide, Panthenol.',
        'how_to_use': 'Apply a sufficient amount to palms and gently massage onto clean face and neck. For very dry skin, apply a thick layer at night and leave as an overnight mask. Use morning and evening.',
        'benefits': 'Rebuilds weakened skin barrier\nPrevents moisture loss\nDeeply moisturizes very dry skin\nLeaves skin silky smooth\nGreat for cold weather',
        'meta_title': 'Dr. Althea 147 Barrier Cream 50ml | Dry Skin | Pendo Essence',
        'meta_description': 'Dr. Althea 147 Barrier Cream with Ceramides and Hyaluronic Acid restores skin barrier and moisturizes dry skin. Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'The Ordinary Natural Moisturizing Factor + HA',
        'brand': 'The Ordinary',
        'size': '30ml',
        'skin_type': 'all',
        'price': 18000,
        'compare_price': 24000,
        'stock': 45,
        'is_featured': True,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'A simple yet powerful moisturizer — NMF and Hyaluronic Acid for lasting skin hydration.',
        'description': (
            'The Ordinary Natural Moisturizing Factor + HA is a moisturizer that proves the best doesn\'t have to be expensive. '
            'NMF (Natural Moisturizing Factors) is a combination of amino acids, sugars, urea and lactic acid '
            'that naturally exist in our skin — keeping it moisturized. '
            'This product replenishes NMF that is lost due to age, environment or fatigue. '
            'Multi-molecular weight Hyaluronic Acid absorbs moisture from the air '
            'and holds it within the skin. '
            'This light, non-greasy formula is suitable for all skin types and can be used '
            'under SPF or makeup without being visible.'
        ),
        'ingredients': 'Sodium Hyaluronate (HA), Amino Acids (Glycine, Alanine, Glutamic Acid), PCA, Lactic Acid, Urea, Allantoin, Glycerin, Ceramide NP, Sodium PCA.',
        'how_to_use': 'After toner or serum, apply a small amount to fingertips and massage onto face until absorbed. Can be used morning and evening. Follow with SPF in the morning.',
        'benefits': 'Replenishes lost NMF in skin\nRetains moisture for longer\nLight and invisible on skin\nSuitable for all skin types\nExcellent value for this quality',
        'meta_title': 'The Ordinary Natural Moisturizing Factor + HA 30ml | Pendo Essence',
        'meta_description': 'The Ordinary Natural Moisturizing Factor + HA is a light moisturizer with NMF and Hyaluronic Acid for lasting hydration. Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'COSRX Hyaluronic Acid Intensive Cream',
        'brand': 'COSRX',
        'size': '100g',
        'skin_type': 'dry',
        'price': 38000,
        'compare_price': 46000,
        'stock': 18,
        'is_featured': False,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'Moisturize with the power of Hyaluronic Acid — a K-beauty cream that deeply nourishes dry skin.',
        'description': (
            'COSRX Hyaluronic Acid Intensive Cream is a true dream for people with dry skin. '
            'It is packed with multi-weight Hyaluronic Acid that works at different layers of the skin — '
            'high-weight HA stays on top of skin, creating a protective moisture barrier; '
            'medium-weight HA penetrates the upper skin layers; '
            'low-weight HA penetrates deeper. '
            'The result? True moisture from the inside out. '
            'This rich cream is particularly great at night, or for people living in dry or very cold environments. '
            'Even after just a few initial hours, skin feels soft and alive.'
        ),
        'ingredients': 'Hyaluronic Acid (Multi-weight), Sodium Hyaluronate, Panthenol, Ceramide NP, Beta-Glucan, Arginine, Glycerin, Squalane.',
        'how_to_use': 'Night: After toner and serum, apply a sufficient amount to fingertips and massage in circular motions onto face. Morning: Apply a small amount as a base moisturizer. Follow with SPF.',
        'benefits': 'Deeply hydrates with multi-weight HA\nMakes dry skin silky smooth\nGreat as a night moisturizer\nPrevents premature wrinkles\nLeaves skin looking alive in the morning',
        'meta_title': 'COSRX Hyaluronic Acid Intensive Cream 100g | Dry Skin | Pendo Essence',
        'meta_description': 'COSRX Hyaluronic Acid Intensive Cream deeply nourishes dry skin with the power of multi-weight HA. K-beauty Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'Oh So Heavenly Dark Spot Corrector',
        'brand': 'Oh So Heavenly',
        'size': '30ml',
        'skin_type': 'all',
        'price': 20000,
        'compare_price': 26000,
        'stock': 22,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Fade dark spots — a serum/moisturizer perfectly formulated for darker skin tones.',
        'description': (
            'Oh So Heavenly Dark Spot Corrector is designed specifically for darker skin tones struggling with hyperpigmentation, '
            'post-acne marks (PIH - Post Inflammatory Hyperpigmentation), and uneven skin tone. '
            'Its brightening ingredients work by inhibiting melanin production '
            'in areas with dark spots. '
            'Niacinamide, Vitamin C and Kojic Acid combine to deliver fast and lasting results. '
            'This is not a regular cream — it is a targeted corrector, suitable for specific areas or the whole face. '
            'Many African women say this is one of the best products for their skin.'
        ),
        'ingredients': 'Niacinamide 5%, Kojic Acid, Vitamin C (Ascorbic Acid), Alpha Arbutin, Licorice Root Extract, Glycerin, Hyaluronic Acid.',
        'how_to_use': 'After cleanser and toner, apply a small amount to spotted areas or the whole face. Massage gently. Follow with moisturizer. Use morning and evening. Always wear SPF in the morning.',
        'benefits': 'Fades dark spots and hyperpigmentation\nEvens out skin tone\nImproves skin radiance\nSuitable for darker skin tones\nResults visible within 2-4 weeks',
        'meta_title': 'Oh So Heavenly Dark Spot Corrector 30ml | Hyperpigmentation | Pendo Essence',
        'meta_description': 'Oh So Heavenly Dark Spot Corrector fades dark spots and evens out skin tone. Best for darker skin tones. Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'NIVEA Vitamin E Day Cream Moisturiser',
        'brand': 'NIVEA',
        'size': '50ml',
        'skin_type': 'normal',
        'price': 16000,
        'compare_price': 20000,
        'stock': 50,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Daily protection with Vitamin E — a simple moisturizer that fights signs of aging.',
        'description': (
            'NIVEA Vitamin E Day Cream is a simple everyday moisturizer that provides basic protection for your skin. '
            'Vitamin E (Tocopherol) is a powerful antioxidant that fights free radicals that cause premature aging. '
            'It prevents damage caused by sun rays, air pollution and stress. '
            'Its light formula absorbs quickly without leaving grease behind. '
            'Suitable for normal to dry skin and can be used as a makeup base. '
            'Its affordable price makes it a great choice for those just starting their skincare journey.'
        ),
        'ingredients': 'Vitamin E (Tocopheryl Acetate), Glycerin, Petrolatum, Shea Butter, Panthenol, Allantoin, Glycol Stearate.',
        'how_to_use': 'Apply a small amount to fingertips and gently massage onto face and neck in the morning after cleansing. Can be used as a base before makeup. Use every day.',
        'benefits': 'Protects against free radical damage\nMoisturizes skin\nAbsorbs quickly\nSuitable as a makeup base\nAffordable and easy to find',
        'meta_title': 'NIVEA Vitamin E Day Cream 50ml | Daily Moisturizer | Pendo Essence',
        'meta_description': 'NIVEA Vitamin E Day Cream protects and moisturizes your skin every day with the power of Vitamin E. Simple moisturizer Tanzania.',
    },
    {
        'category_slug': 'moisturisers',
        'name': 'Anti-Melasma Cica Cream',
        'brand': 'Pendo Essence',
        'size': '40ml',
        'skin_type': 'sensitive',
        'price': 35000,
        'compare_price': 44000,
        'stock': 12,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': True,
        'short_description': 'Fight melasma and dark spots — a powerful Cica cream that improves African skin tone.',
        'description': (
            'Anti-Melasma Cica Cream is designed specifically for darker skin tones struggling with melasma — '
            'large brown patches that appear on the face, especially on the forehead, cheeks and chin. '
            'Melasma is often caused by hormonal changes, pregnancy, or sun exposure. '
            'This cream combines the power of Centella Asiatica (calming irritated skin) '
            'with melanin-inhibiting ingredients (Alpha Arbutin, Kojic Acid, Tranexamic Acid) '
            'to create a two-pronged approach: soothing and improving skin tone. '
            'Particularly great after laser melasma treatments, or as a regular daily treatment.'
        ),
        'ingredients': 'Centella Asiatica Extract 50%, Tranexamic Acid 2%, Alpha Arbutin 1%, Kojic Acid 1%, Niacinamide 5%, Licorice Root Extract, Hyaluronic Acid, Ceramide NP.',
        'how_to_use': 'Use in the evening and/or night. After cleanser and toner, apply a sufficient amount to fingertips and gently massage onto spotted areas or the whole face. MUST wear SPF 50+ every morning without fail.',
        'benefits': 'Fights melasma and melanin spots\nCalms irritated skin\nImproves skin tone\nSuitable for post-laser skin\nShows results within 4-8 weeks',
        'meta_title': 'Anti-Melasma Cica Cream 40ml | Dark Spots | Pendo Essence',
        'meta_description': 'Anti-Melasma Cica Cream with Centella and brightening agents that fights melasma for darker skin tones. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # DEODORANTS
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'deodorants',
        'name': 'Mitchum Women Unscented Deodorant',
        'brand': 'Mitchum',
        'size': '63g',
        'skin_type': 'sensitive',
        'price': 18000,
        'compare_price': 23000,
        'stock': 30,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': '48-hour protection with no scent — the best deodorant for sensitive skin and those allergic to fragrances.',
        'description': (
            'Mitchum Women Unscented is the best choice for women who have sensitive skin under their arms. '
            'Its Triple Odor Defense formula works in three ways: it prevents excessive sweating, '
            'eliminates odor-causing bacteria, and has odor-absorbing technology that traps odor. '
            'Being completely unscented, it is great for people with fragrance allergies, '
            'those who prefer their own special perfume, or those using other scented body products. '
            'Its 48-hour protection means even after a full night or a long work day, you stay fresh.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclopentasiloxane, Stearyl Alcohol, PPG-14 Butyl Ether, Hydrogenated Castor Oil, Talc.',
        'how_to_use': 'Apply to clean underarm areas in the morning after bathing. Wait to dry before dressing. Can be used at night for better morning protection.',
        'benefits': '48-hour protection\nNo fragrance — great for sensitive skin\nPrevents excessive sweating\nHolds odor all day\nGreat for those who wear their own perfume',
        'meta_title': 'Mitchum Women Unscented Deodorant 63g | Sensitive Skin | Pendo Essence',
        'meta_description': 'Mitchum Women Unscented Deodorant provides 48-hour protection with no scent. Best for sensitive skin and fragrance-free lifestyle. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Mitchum Women Shower Fresh Deodorant',
        'brand': 'Mitchum',
        'size': '63g',
        'skin_type': 'all',
        'price': 18000,
        'compare_price': 23000,
        'stock': 30,
        'is_featured': False,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'Feel fresh all the time — Mitchum Shower Fresh gives you that just-showered feeling all day long.',
        'description': (
            'Mitchum Women Shower Fresh is a deodorant that delivers a clean and refreshing feeling as if you just showered, '
            'even after many hours. '
            'Its Shower Fresh scent is refreshing but not overpowering — it blends well with fragrances '
            'or feels great on its own. '
            'Its Triple Odor Defense Technology delivers 48-hour protection — '
            'twice as long as regular deodorants. '
            'Great for working women who don\'t have time to shower often or need to '
            'feel clean throughout the whole day.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclopentasiloxane, Stearyl Alcohol, PPG-14 Butyl Ether, Fragrance (Shower Fresh), Hydrogenated Castor Oil.',
        'how_to_use': 'Apply to clean underarm areas. Wait to dry before dressing. For best protection, use at night before bed and in the morning.',
        'benefits': 'Just-showered feeling all day\n48-hour protection\nLight and refreshing scent\nDoes not leave stains on clothes\nGreat for working women',
        'meta_title': 'Mitchum Women Shower Fresh Deodorant 63g | Pendo Essence',
        'meta_description': 'Mitchum Women Shower Fresh Deodorant delivers a fresh and refreshing feeling with 48-hour protection. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Mitchum Women Flowers Fresh Deodorant',
        'brand': 'Mitchum',
        'size': '63g',
        'skin_type': 'all',
        'price': 18000,
        'compare_price': 23000,
        'stock': 25,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'A gentle floral scent — Mitchum Flowers Fresh gives you a sense of softness and femininity all day.',
        'description': (
            'Mitchum Women Flowers Fresh is a deodorant that brings a gentle and unique floral feeling. '
            'Its floral scent is high quality, not harsh or unpleasant, but light and lovely '
            'that lasts for many hours. '
            'Like all Mitchum deodorants, it has Triple Odor Defense and 48-hour protection. '
            'Great for women who love feeling feminine and lovely without worrying about sweat or bad odor. '
            'Its attractive purple bottle makes it a lovely product to show off in your bathroom.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclopentasiloxane, Stearyl Alcohol, PPG-14 Butyl Ether, Fragrance (Flowers), Vitamin E.',
        'how_to_use': 'Apply to clean underarm areas. Wait 30 seconds to dry before dressing. Can be used morning and night.',
        'benefits': 'Gentle and lovely floral scent\n48-hour protection\nPrevents excessive sweating\nLeaves skin soft\nDoes not leave marks on white clothes',
        'meta_title': 'Mitchum Women Flowers Fresh Deodorant 63g | Pendo Essence',
        'meta_description': 'Mitchum Women Flowers Fresh Deodorant with a gentle floral scent and 48-hour protection. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Saltair Santal Bloom 5% AHA Serum Deodorant',
        'brand': 'Saltair',
        'size': '85g',
        'skin_type': 'sensitive',
        'price': 32000,
        'compare_price': 40000,
        'stock': 12,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': True,
        'short_description': 'A modern skincare deodorant — AHA that makes underarm skin smooth and clean.',
        'description': (
            'Saltair Santal Bloom is more than a deodorant — it is underarm skincare. '
            'Many deodorants block sweat with aluminum, but Saltair takes a different approach: '
            '5% AHA (Glycolic Acid) that exfoliates underarm skin, removing dead skin cells '
            'that can cause odor and make skin rough. '
            'After a few weeks of use, the results: underarm skin becomes smoother, '
            'lighter (helps reduce underarm hyperpigmentation that bothers many African people), '
            'and its luxurious Sandalwood scent makes you feel premium. '
            'Aluminum-free, baking soda-free — best for sensitive skin.'
        ),
        'ingredients': 'Glycolic Acid 5%, Sodium Bicarbonate Free Formula, Caprylic/Capric Triglyceride, Shea Butter, Arrowroot Powder, Sandalwood Fragrance, Aloe Vera.',
        'how_to_use': 'Apply a small amount to the underarm area. Rub gently. For first-time use, start every two days until skin adjusts to AHA. Use daily once skin has adjusted.',
        'benefits': 'Exfoliates underarm skin\nReduces underarm hyperpigmentation\nLeaves skin smooth and clean\nAluminum-free\nLuxurious Sandalwood scent',
        'meta_title': 'Saltair Santal Bloom AHA Serum Deodorant | Pendo Essence Tanzania',
        'meta_description': 'Saltair Santal Bloom Deodorant has 5% AHA that smooths and improves underarm skin. Aluminum-free. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Secret Cozy Vanilla Deodorant',
        'brand': 'Secret',
        'size': '73g',
        'skin_type': 'all',
        'price': 20000,
        'compare_price': 25000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'A gentle vanilla scent — 48-hour protection with a cozy and lovely fragrance.',
        'description': (
            'Secret Cozy Vanilla is a deodorant that brings warmth and calm with its gentle vanilla scent. '
            'Vanilla is one of the most loved scents in the world — it makes people feel welcomed, '
            'peaceful and attractive. '
            'It has Secret\'s MotionSense Technology that creates tiny fragrance capsules '
            'that break when they contact your skin, releasing fresh scent every time you move. '
            'Its 48-hour protection means even on a sports day or a long work day, you stay fresh and lovely.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclopentasiloxane, PPG-14 Butyl Ether, Stearyl Alcohol, Vanilla Extract, Fragrance.',
        'how_to_use': 'Apply to clean underarm areas in the morning. Wait to dry before dressing. Use daily or as needed.',
        'benefits': 'Cozy and lovely vanilla scent\nMotionSense technology releases fresh scent every time you move\n48-hour protection\nPrevents excessive sweating\nDoes not leave stains on clothes',
        'meta_title': 'Secret Cozy Vanilla Deodorant 73g | Pendo Essence Tanzania',
        'meta_description': 'Secret Cozy Vanilla Deodorant with a gentle vanilla scent and 48-hour protection. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Secret Outlast Deodorant',
        'brand': 'Secret',
        'size': '73g',
        'skin_type': 'all',
        'price': 20000,
        'compare_price': 25000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Built to last longer — Secret Outlast delivers all-day protection without fail.',
        'description': (
            'Secret Outlast is designed for people whose lives require them to work hard — '
            'those who have no time to worry about deodorant running out early. '
            'Its 48-hour protection means you can go to work, hit the gym, '
            'or attend an evening event without any worry whatsoever. '
            'Its "Completely Clean" scent is gentle, clean and pleasant — '
            'great for women who prefer a scent that doesn\'t overpower their perfume. '
            'Its odor neutralization formula works deep down, not just masking odor but eliminating it completely.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclopentasiloxane, Stearyl Alcohol, PPG-14 Butyl Ether, Hydrogenated Castor Oil, Fragrance (Clean).',
        'how_to_use': 'Apply to clean underarm areas. Wait to dry. For best protection, use at night before bed.',
        'benefits': 'Powerful 48-hour protection\nWorks even on long work days\nClean and gentle scent\nTrue odor neutralization\nGreat for a busy lifestyle',
        'meta_title': 'Secret Outlast Deodorant 73g | 48-Hour Protection | Pendo Essence',
        'meta_description': 'Secret Outlast Deodorant provides 48-hour protection with a clean scent. Best for a busy lifestyle. Tanzania.',
    },
    {
        'category_slug': 'deodorants',
        'name': 'Old Spice Original Rich Scent Deodorant',
        'brand': 'Old Spice',
        'size': '50ml',
        'skin_type': 'all',
        'price': 16000,
        'compare_price': 20000,
        'stock': 35,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'The classic masculine scent — Old Spice Original with a gentle and lasting powerful fragrance.',
        'description': (
            'Old Spice Original is more than a deodorant — it is part of masculine cultural history. '
            'Since 1938, its unique spicy, woody and citrus scent has been defining "being a man." '
            'Its formula has been improved over many years but still carries that classic beloved feeling. '
            'It protects against sweat odor, brings a refreshing feeling and makes you feel confident. '
            'Suitable for every man — from young people starting their journey to older men who love the classics. '
            'Its iconic red plastic bottle represents enduring quality.'
        ),
        'ingredients': 'Aluminum Zirconium Tetrachlorohydrex GLY, Cyclomethicone, Fragrance (Original Spice Blend), Talc, PPG-14 Butyl Ether.',
        'how_to_use': 'Apply to clean underarm areas in the morning. Wait to dry. Use daily for a gentle and classic scent all day.',
        'benefits': 'Classic masculine scent that lasts\nEffectively prevents sweat odor\n24-hour protection\nGreat value for this quality\nA globally trusted brand for 85+ years',
        'meta_title': 'Old Spice Original Deodorant 50ml | Men | Pendo Essence',
        'meta_description': 'Old Spice Original Deodorant with a classic lasting masculine scent. Best for men. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # HAIR REMOVAL
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'hair-removal',
        'name': 'No Hair Cream Charglow',
        'brand': 'No Hair',
        'size': '150ml',
        'skin_type': 'all',
        'price': 16000,
        'compare_price': 20000,
        'stock': 25,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Remove hair painlessly — a gentle cream that works within 5-10 minutes.',
        'description': (
            'No Hair Charglow is a hair removal cream that works quickly and without the pain of shaving. '
            'Its powerful formula penetrates the hair, breaking down its protein structure (keratin) '
            'until the hair becomes soft and can be wiped away easily. '
            'Results last longer than blade shaving, '
            'because it removes hair from the base of the skin rather than the surface. '
            'Its scent has been improved to be tolerable and pleasant. '
            'Suitable for legs, arms and other body areas (not for the face or very sensitive areas).'
        ),
        'ingredients': 'Thioglycolic Acid, Calcium Hydroxide, Mineral Oil, Cetearyl Alcohol, Aloe Vera, Vitamin E, Parfum.',
        'how_to_use': 'Apply cream evenly to the desired area in sufficient quantity. Wait 5-10 minutes (do not exceed 15 minutes). Wipe off with the spatula included in the packaging or a soft sponge. Rinse thoroughly with cold water. Do a patch test first.',
        'benefits': 'Removes hair painlessly\nWorks within 5-10 minutes\nResults last longer\nLeaves skin smooth\nEasy to use at home',
        'meta_title': 'No Hair Charglow Cream 150ml | Hair Removal | Pendo Essence',
        'meta_description': 'No Hair Charglow cream removes hair painlessly within 5-10 minutes for smooth skin. Tanzania.',
    },
    {
        'category_slug': 'hair-removal',
        'name': 'No Hair Men with Conditioning Oil',
        'brand': 'No Hair',
        'size': '150ml',
        'skin_type': 'all',
        'price': 16000,
        'compare_price': 20000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Designed for men — a powerful cream for coarse hair with soft skin after.',
        'description': (
            'No Hair Men with Conditioning Oil is designed specifically for men\'s hair which is often thicker '
            'and tougher than women\'s. '
            'Its powerful formula removes tough hair quickly while the added Conditioning Oil '
            'ensures skin stays soft and moisturized after treatment. '
            'For men who want an alternative to blade shaving — especially areas like the back, chest, or arms — '
            'this is the best painless solution without the pain of ingrown hairs or post-shave bumps.'
        ),
        'ingredients': 'Thioglycolic Acid, Calcium Hydroxide, Mineral Oil, Conditioning Oils (Argan, Jojoba), Cetearyl Alcohol, Aloe Vera, Parfum.',
        'how_to_use': 'Apply cream sufficiently to the desired area. Wait 8-12 minutes for coarse hair. Wipe off with a wet sponge or soft cloth. Rinse thoroughly with water. Do a patch test before first use.',
        'benefits': 'Powerful formula for men\'s coarse hair\nConditioning oils leave skin smooth\nNo ingrown hairs\nEasy to use\nNo blades — no risk of cuts',
        'meta_title': 'No Hair Men with Conditioning Oil 150ml | Men | Pendo Essence',
        'meta_description': 'No Hair Men Cream has conditioning oils for men. Removes coarse hair painlessly and leaves skin smooth. Tanzania.',
    },
    {
        'category_slug': 'hair-removal',
        'name': 'Vaya Smooth Hair Removal Cream for Men',
        'brand': 'Vaya',
        'size': '150ml',
        'skin_type': 'all',
        'price': 18000,
        'compare_price': 23000,
        'stock': 18,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Smooth and clean for men — Vaya Smooth delivers quick results and lovely skin.',
        'description': (
            'Vaya Smooth for Men is a hair removal cream that delivers quick results for coarse hair. '
            'It works within 8-12 minutes and leaves skin smooth for much longer than shaving. '
            'Its formula is enhanced with moisturizers that help reduce redness and irritation '
            'that can occur after hair removal. '
            'Suitable for arms, legs, chest and back. '
            'Its masculine scent makes it a comfortable product to use.'
        ),
        'ingredients': 'Thioglycolic Acid, Potassium Hydroxide, Cetearyl Alcohol, Glycerin, Aloe Vera, Masculine Fragrance, Panthenol.',
        'how_to_use': 'Apply cream sufficiently to desired areas. Wait 8-12 minutes. Wipe off with a wet sponge or spatula. Rinse well with cold water. Caution: do not use on sensitive areas.',
        'benefits': 'Powerful formula for men\'s coarse hair\nNo shaving pain\nResults last longer\nLeaves skin smooth and clean\nPleasant masculine scent',
        'meta_title': 'Vaya Smooth Hair Removal Cream Men 150ml | Pendo Essence',
        'meta_description': 'Vaya Smooth for Men removes hair quickly and leaves skin very smooth. Tanzania.',
    },
    {
        'category_slug': 'hair-removal',
        'name': 'Vaya Smooth Hair Removal Cream for Women',
        'brand': 'Vaya',
        'size': '150ml',
        'skin_type': 'sensitive',
        'price': 18000,
        'compare_price': 23000,
        'stock': 22,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Smooth and beautiful for women — Vaya Smooth removes hair and leaves skin silky smooth.',
        'description': (
            'Vaya Smooth for Women is designed with the unique needs of women\'s skin in mind. '
            'Its gentle formula removes leg, arm and other area hair more gently '
            'than the men\'s version, considering that women\'s skin is often more sensitive. '
            'Moisturizing agents kick in from the very first use, '
            'leaving skin smooth, hydrated and lovely long after application. '
            'Its beautiful floral scent makes the hair removal treatment a more pleasant experience.'
        ),
        'ingredients': 'Thioglycolic Acid, Calcium Hydroxide, Shea Butter, Rose Extract, Aloe Vera, Glycerin, Floral Fragrance, Panthenol, Vitamin E.',
        'how_to_use': 'Apply cream sufficiently to desired areas. Wait 6-10 minutes. Wipe off with a wet sponge or spatula. Rinse well with cold water. Apply moisturizer afterward.',
        'benefits': 'Gentle formula suitable for women\'s sensitive skin\nLeaves skin silky smooth\nResults last longer\nBeautiful floral scent\nMoisturizing ingredients continue working',
        'meta_title': 'Vaya Smooth Hair Removal Cream Women 150ml | Pendo Essence',
        'meta_description': 'Vaya Smooth for Women removes hair gently and leaves skin silky smooth. Tanzania.',
    },
    {
        'category_slug': 'hair-removal',
        'name': 'EOS Cashmere Shave Oil Pink Champagne',
        'brand': 'EOS',
        'size': '177ml',
        'skin_type': 'sensitive',
        'price': 28000,
        'compare_price': 35000,
        'stock': 14,
        'is_featured': True,
        'is_bestseller': False,
        'is_natural': True,
        'short_description': 'Shave in luxury — a premium shave oil that protects against razor bumps and leaves skin smooth.',
        'description': (
            'EOS Cashmere Shave Oil is a true game-changer for those who suffer from ingrown hairs, '
            'post-shave bumps, or dry skin after shaving. '
            'Unlike regular foams or gels, this oil creates a protective layer between blade and skin, '
            'allowing the blade to glide much more smoothly and significantly reducing the chance of cuts. '
            'Its Pink Champagne scent is refreshing, feminine and luxurious. '
            'Particularly great for sensitive areas like the bikini line, face (for women) and legs. '
            'After shaving, skin remains moisturized and smooth because the oil stays slightly on the skin.'
        ),
        'ingredients': 'Sunflower Oil, Castor Oil, Vitamin E, Jojoba Oil, Aloe Vera, Pink Champagne Fragrance, Grapefruit Extract.',
        'how_to_use': 'Wet skin with warm water. Apply 3-5 drops to your hands or directly onto skin. Massage gently and place your blade and shave smoothly. Rinse well afterward.',
        'benefits': 'Blade glides smoothly — no nicking\nReduces ingrown hairs\nLeaves skin smooth and moisturized\nLuxurious Pink Champagne scent\nSuitable for sensitive areas',
        'meta_title': 'EOS Cashmere Shave Oil Pink Champagne 177ml | Pendo Essence',
        'meta_description': 'EOS Cashmere Shave Oil makes shaving a luxury experience while protecting against bumps and leaving skin smooth. Tanzania.',
    },
    {
        'category_slug': 'hair-removal',
        'name': 'NIVEA Men Shaving Foam',
        'brand': 'NIVEA',
        'size': '193g',
        'skin_type': 'sensitive',
        'price': 14000,
        'compare_price': 18000,
        'stock': 30,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'The classic men\'s shave — NIVEA foam that protects and softens skin while shaving.',
        'description': (
            'NIVEA Men Shaving Foam is a product trusted by men worldwide for many years. '
            'Its gentle foam creates a protective layer between blade and skin, making the blade glide smoothly '
            'and reducing the chance of cuts, nicks or post-shave bumps (razor bumps). '
            'Added Provitamin B5 nourishes and protects skin, ensuring that even after shaving '
            'skin feels comfortable and smooth. '
            'Suitable for all beard types — from soft to tough. '
            'Produces a large amount of foam from a small amount, making the can last a long time.'
        ),
        'ingredients': 'Aqua, Stearic Acid, Triethanolamine, Isobutane, Propane, Glycerin, Panthenol (Pro-Vitamin B5), Parfum, Chamomile Extract.',
        'how_to_use': 'Wet beard with warm water for 30-60 seconds. Apply sufficient foam to hands and spread onto face. Massage in circular motions. Shave in the direction of beard growth. Rinse thoroughly.',
        'benefits': 'Gentle foam allows blade to glide\nReduces bumps and ingrown hairs\nProvitamin B5 nourishes skin\nProduces large amount of foam\nSuitable for all beard types',
        'meta_title': 'NIVEA Men Shaving Foam 193g | Shaving | Pendo Essence Tanzania',
        'meta_description': 'NIVEA Men Shaving Foam with Provitamin B5 makes shaving smooth and protects skin. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # FEMININE WASH
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'feminine-wash',
        'name': 'Femfresh Active Wash',
        'brand': 'Femfresh',
        'size': '250ml',
        'skin_type': 'sensitive',
        'price': 24000,
        'compare_price': 30000,
        'stock': 25,
        'is_featured': True,
        'is_bestseller': True,
        'is_natural': False,
        'short_description': 'Intimate hygiene for active women — the right pH and protection against odor.',
        'description': (
            'Femfresh Active Wash is designed for working women with busy lives '
            'who need to feel fully confident at all times. '
            'It has a pH balance of 4.5 — matching the natural pH of the intimate area — '
            'which preserves the natural environment of good bacteria (flora) '
            'and prevents the growth of bacteria and fungi that cause infections. '
            'Unlike regular soaps which have a high pH (7-9) that disrupts natural flora, '
            'Femfresh maintains the body\'s natural self-defence system. '
            'Suitable for daily use, even during menstruation or after exercise.'
        ),
        'ingredients': 'Aqua, Sodium Laureth Sulfate, Cocamidopropyl Betaine, Sodium Chloride, Lactic Acid, Citric Acid, Panthenol, Aloe Vera, Fragrance (Active Fresh).',
        'how_to_use': 'Apply a small amount to your hand or a soft sponge. Gently cleanse the external intimate area in circular motions. NEVER use internally. Rinse well with water. Can be used daily.',
        'benefits': 'Correct pH (4.5) for intimate areas\nPrevents bacterial and fungal infections\nPrevents unpleasant odor\nSuitable for daily use\nLeaves a clean and refreshing feeling',
        'meta_title': 'Femfresh Active Wash 250ml | Feminine Wash | Pendo Essence',
        'meta_description': 'Femfresh Active Wash has the correct pH for women\'s intimate areas. Prevents infections and odor. Tanzania.',
    },
    {
        'category_slug': 'feminine-wash',
        'name': 'Femfresh 0% Sensitive Wash',
        'brand': 'Femfresh',
        'size': '250ml',
        'skin_type': 'sensitive',
        'price': 26000,
        'compare_price': 32000,
        'stock': 20,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Maximum gentleness — no fragrance, no dye, no harsh chemicals. Best for very sensitive skin.',
        'description': (
            'Femfresh 0% Sensitive Wash is designed for women with very sensitive skin or those who frequently experience '
            'itching, burning or recurring intimate area problems. '
            '"0%" represents: 0% artificial fragrance, 0% artificial colours, 0% alcohol, 0% parabens. '
            'Its completely pure formula cleanses with maximum gentleness without affecting natural flora. '
            'Doctors recommend it for women recovering from yeast infections or bacterial vaginosis, '
            'pregnant women, the elderly, and all those with sensitive skin. '
            'Also suitable for women going through hormonal changes (menopause).'
        ),
        'ingredients': 'Aqua, Sodium Laureth Sulfate, Cocamidopropyl Betaine, Glycerin, Lactic Acid, Citric Acid, Panthenol, Aloe Vera, Sodium Hydroxide.',
        'how_to_use': 'Apply a small amount to your hand or soft cotton. Cleanse the external area very gently. NEVER use internally. Rinse well with cold water. Can be used daily.',
        'benefits': '0% fragrance, dye, alcohol or parabens\nMaximum gentleness formula\nRecommended for very sensitive skin\nSuitable during recovery from infections\nHelps maintain natural flora',
        'meta_title': 'Femfresh 0% Sensitive Wash 250ml | Sensitive Skin | Pendo Essence',
        'meta_description': 'Femfresh 0% Sensitive Wash with no fragrance, dye or harsh chemicals. Best for very sensitive skin. Tanzania.',
    },
    {
        'category_slug': 'feminine-wash',
        'name': 'Gynaguard Intimate Wash',
        'brand': 'Gynaguard',
        'size': '140ml',
        'skin_type': 'sensitive',
        'price': 20000,
        'compare_price': 25000,
        'stock': 22,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'Deep intimate protection — Gynaguard is recommended by gynecologists.',
        'description': (
            'Gynaguard Intimate Wash is developed in collaboration with gynecologists '
            'to ensure it truly meets the intimate hygiene needs of women. '
            'Its formula contains Lactic Acid that maintains the natural pH (3.8-4.5), '
            'Lactobacillus that supports the growth of good bacteria, '
            'and antibacterial ingredients that prevent the growth of potentially harmful organisms. '
            'Particularly great for women in Tanzania who are often affected by hot and humid weather '
            'that can increase the risk of infections. '
            'Recommended for use twice daily for optimal hygiene.'
        ),
        'ingredients': 'Aqua, Lactic Acid, Lactobacillus Ferment, Sodium Laureth Sulfate (mild), Aloe Vera, Calendula Extract, Panthenol, Glycerin.',
        'how_to_use': 'Apply a small amount to wet hands. Gently cleanse the external intimate areas. Rinse thoroughly. Use morning and evening for best hygiene. Extended washing is not necessary.',
        'benefits': 'Developed by gynecologists\nMaintains natural pH (3.8-4.5)\nPromotes good flora (Lactobacillus)\nPrevents common infections\nRecommended for hot weather',
        'meta_title': 'Gynaguard Intimate Wash 140ml | Doctor Recommended | Pendo Essence',
        'meta_description': 'Gynaguard Intimate Wash developed by gynecologists. Protects and balances the natural flora of intimate areas. Tanzania.',
    },
    {
        'category_slug': 'feminine-wash',
        'name': 'Feminine Intimate Deodorant Spray',
        'brand': 'Pendo Essence',
        'size': '150ml',
        'skin_type': 'sensitive',
        'price': 18000,
        'compare_price': 23000,
        'stock': 15,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': False,
        'short_description': 'An intimate spray — quick clean and refreshing feeling whenever you need it.',
        'description': (
            'Feminine Intimate Deodorant Spray is a quick and easy solution for whenever you need to '
            'feel clean and refreshed without time to shower. '
            'Suitable for external intimate area use, '
            'delivering a quick feeling of cleanliness and preventing unpleasant odor. '
            'Great for travel, after exercise, during menstruation or whenever you need '
            'to feel clean quickly. '
            'Its formula has a pH neutralizer that works quickly '
            'and gentle ingredients that protect sensitive skin.'
        ),
        'ingredients': 'Aqua, Alcohol Denat., Glycerin, Aloe Vera, Lactic Acid, Chamomile Extract, Fresh Floral Fragrance, Panthenol.',
        'how_to_use': 'Shake well. Spray a small amount (15-20 cm away) onto external intimate areas. Let dry. Do not use internally. Can also be used on underwear.',
        'benefits': 'Quick and easy to use\nGreat for travel and emergencies\nPrevents unpleasant odor\nGentle formula for sensitive skin\nLeaves a quick refreshing feeling',
        'meta_title': 'Feminine Intimate Deodorant Spray | Pendo Essence Tanzania',
        'meta_description': 'Feminine Intimate Deodorant Spray gives quick cleanliness and freshness whenever you need it. Great for travel. Tanzania.',
    },

    # ══════════════════════════════════════════════════════════════
    # ACCESSORIES
    # ══════════════════════════════════════════════════════════════
    {
        'category_slug': 'accessories',
        'name': 'Cotton Pads Premium',
        'brand': 'Pendo Essence',
        'size': '80 Pads',
        'skin_type': 'all',
        'price': 8000,
        'compare_price': 10000,
        'stock': 80,
        'is_featured': False,
        'is_bestseller': False,
        'is_natural': True,
        'short_description': 'Premium quality soft cotton pads — best for toner, makeup removal and skin treatments.',
        'description': (
            'Cotton Pads Premium are an essential skincare tool used every day. '
            'They are made from 100% pure natural cotton without bleaching chemicals or added ingredients. '
            'Their high-quality softness makes them ideal for sensitive skin and skincare treatments that require a careful routine. '
            'Suitable for: applying toner evenly, gently removing makeup, applying micellar water, '
            'applying AHA/BHA toner (like Glycolic Acid), and spot treatment for acne. '
            'You can also soak them in toner and place them as a 10-minute mask on dry areas. '
            'Each pack has 80 pads, enough for about one month of daily use.'
        ),
        'ingredients': '100% pure natural cotton. Contains no fragrance, bleach or other chemicals.',
        'how_to_use': 'For toner: Pour a small amount of toner onto the pad, massage in circular motions onto clean face. For makeup removal: Soak pad in micellar water or makeup remover, gently reach eyes and face. Dispose after use.',
        'benefits': '100% pure natural cotton\nHigh-quality softness for sensitive skin\nSuitable for many different uses\nCan be used as a mini mask\nGreat value for 80 pads',
        'meta_title': 'Cotton Pads Premium 80 Pads | Skincare | Pendo Essence Tanzania',
        'meta_description': 'Cotton Pads Premium made from 100% pure cotton. Best for toner, makeup removal and skincare treatments. 80 pads. Tanzania.',
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# INSERT PRODUCTS
# ─────────────────────────────────────────────────────────────────────────────

success = 0
errors = 0

for p in products_data:
    try:
        cat = cats[p['category_slug']]
        obj, created = Product.objects.update_or_create(
            name=p['name'],
            size=p.get('size', ''),
            defaults={
                'category': cat,
                'brand': p.get('brand', ''),
                'description': p.get('description', ''),
                'short_description': p.get('short_description', ''),
                'ingredients': p.get('ingredients', ''),
                'how_to_use': p.get('how_to_use', ''),
                'benefits': p.get('benefits', ''),
                'skin_type': p.get('skin_type', 'all'),
                'price': p.get('price', 0),
                'compare_price': p.get('compare_price'),
                'stock': p.get('stock', 0),
                'is_active': True,
                'is_featured': p.get('is_featured', False),
                'is_bestseller': p.get('is_bestseller', False),
                'is_new_arrival': True,
                'is_natural': p.get('is_natural', False),
                'meta_title': p.get('meta_title', ''),
                'meta_description': p.get('meta_description', ''),
                'image': '',     
                'image2': '',    
                'image3': '',   
            }
        )
        label = '✅ Created' if created else '🔄 Updated'
        print(f"  {label}: [{cat.name}] {obj.name} ({obj.size}) — TSh {obj.price:,}")
        success += 1
    except Exception as e:
        print(f"  ❌ ERROR for '{p.get('name')}': {e}")
        errors += 1

print(f"\n{'='*60}")
print(f"✅ Successful: {success}")
print(f"❌ Failed:     {errors}")
print(f"📦 Total categories: {Category.objects.count()}")
print(f"🛍️  Total products:   {Product.objects.count()}")
print(f"{'='*60}")
print("\n🌿 Pendo Essence data loaded successfully! Welcome.")