# Pendo Essence — Maboresho (Changes Summary)

## Files Zilizobadilishwa

```
pendo_essence_changes/
├── requirements.txt                          ← Badilishwa
├── .env.example                              ← Mpya
├── pendo_essence/
│   └── settings.py                           ← Badilishwa
└── store/
    ├── models.py                             ← Badilishwa
    └── migrations/
        └── 0002_uploadcare_images.py         ← Mpya
```

---

## 1. `requirements.txt` — Mabadiliko

| Removed | Added |
|---------|-------|
| `mysqlclient` | `psycopg2-binary` (PostgreSQL driver) |
| — | `pyuploadcare>=5.0.0` (Uploadcare SDK) |

---

## 2. `settings.py` — Mabadiliko

### Database (PostgreSQL — Supabase)
```python
# KABLA (engine yenye makosa — MySQL driver kwa PostgreSQL)
'ENGINE': 'django.db.backends.mysql',

# BAADA (sahihi)
'ENGINE': 'django.db.backends.postgresql',
```
Pia imeongezwa: `'sslmode': 'require'` — Supabase inahitaji SSL.

### Uploadcare Config Mpya
```python
UPLOADCARE = {
    'pub_key': os.environ.get('UPLOADCARE_PUBLIC_KEY'),
    'secret': os.environ.get('UPLOADCARE_SECRET_KEY'),
}
```

### `pyuploadcare.dj` imeongezwa kwenye `INSTALLED_APPS`

### Credentials zinasomwa kutoka `.env` (salama zaidi)

---

## 3. `models.py` — Mabadiliko

Picha zote zimebadilishwa kutoka Django `ImageField` → Uploadcare `ImageField`:

| Model | Field |
|-------|-------|
| `Category` | `image` |
| `Product` | `image`, `image2`, `image3` |
| `ProductImage` | `image` |

**Faida za Uploadcare:**
- Picha zinahifadhiwa kwenye CDN (si server yako)
- Resize on-the-fly: `image.cdn_url + '-/resize/300x300/'`
- Upload widget mzuri kwenye admin ya Django
- Hakuna `Pillow` required kwa kuonyesha picha

---

## 4. Migration Mpya: `0002_uploadcare_images.py`

Inabadilisha column types za picha kwenye database.

---

## Jinsi ya Kutumia

### Hatua 1 — Install packages
```bash
pip install -r requirements.txt
```

### Hatua 2 — Setup `.env`
```bash
cp .env.example .env
# Hariri .env na credentials zako halisi
```

### Hatua 3 — Run migration
```bash
python manage.py migrate
```

### Hatua 4 — Uploadcare kwenye templates
Picha zinaonyeshwa hivyo (zimebadilika kutoka `{{ product.image.url }}`):
```html
<!-- KABLA -->
<img src="{{ product.image.url }}">

<!-- BAADA — URL moja moja, pia unaweza kuongeza transformations -->
<img src="{{ product.image.cdn_url }}">

<!-- Na resizing ya moja kwa moja kutoka CDN -->
<img src="{{ product.image.cdn_url }}-/resize/600x600/-/format/webp/">
```

### Uploadcare Uploader kwenye Template (Forms)
```html
{% load uploadcare %}
{% uploadcare_widget_url %}  {# kwenye <head> #}

<!-- Kisha form yako kawaida — widget itaonekana automatically #}
{{ form.image }}
```

---

## Supabase — Mambo ya Kujua

- **Host format:** `db.XXXXXXXXXXXXXXXX.supabase.co`
- **Port:** `5432` (PostgreSQL standard)
- **SSL:** Required (imewekwa tayari kwenye settings)
- **Password:** Pata kutoka Supabase Dashboard → Settings → Database

## Uploadcare — Mambo ya Kujua

- **Free tier:** 3,000 uploads + 30GB bandwidth/mwezi — inatosha kuanza
- **Dashboard:** https://uploadcare.com/dashboard/
- **Keys:** `pub_key` (public, salama kwenye frontend) na `secret` (private tu)
