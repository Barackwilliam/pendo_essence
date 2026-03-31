### Pendo Essence — cPanel Deployment Guide
# Complete Step-by-Step Instructions

## STEP 1: Upload Files to cPanel

1. Login to your cPanel account
2. Open **File Manager**
3. Navigate to your domain's root folder (e.g., `public_html/` or a subdomain folder)
4. Create a folder called `pendo_essence/` OUTSIDE `public_html/`
   - Example path: `/home/yourusername/pendo_essence/`
5. Upload all project files to `/home/yourusername/pendo_essence/`
6. Upload only `.htaccess` and `passenger_wsgi.py` to `public_html/`

## STEP 2: Set Up Python Environment in cPanel

1. In cPanel, go to **"Setup Python App"** (or "Python App")
2. Click **"Create Application"**
3. Settings:
   - Python version: **3.10** or **3.11**
   - Application root: `pendo_essence` (or your folder name)
   - Application URL: your domain
   - Application startup file: `pendo_essence/wsgi.py`
   - Application Entry point: `application`
4. Click **Create**

## STEP 3: Install Dependencies

In cPanel Python App, click **"Run pip install"** or use the terminal:

```bash
cd ~/pendo_essence
pip install -r requirements.txt
```

## STEP 4: Configure Settings

Edit `pendo_essence/settings.py`:
1. Change `DEBUG = False`
2. Update `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`
3. Generate a new SECRET_KEY (use: https://djecrety.ir/)
4. Update database settings if using MySQL

## STEP 5: Run Migrations & Setup

In the cPanel terminal or SSH:

```bash
cd ~/pendo_essence
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py shell < populate_data.py
```

## STEP 6: Static Files Configuration

Add to your `public_html/.htaccess`:
```
SetEnvIf Request_URI ^/static/ no_wsgi
SetEnvIf Request_URI ^/media/ no_wsgi
```

Or use WhiteNoise (already in requirements.txt). Add to MIDDLEWARE in settings.py (after SecurityMiddleware):
```python
'whitenoise.middleware.WhiteNoiseMiddleware',
```

Add to settings.py:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## STEP 7: passenger_wsgi.py (place in public_html/)

```python
import sys, os
sys.path.insert(0, '/home/yourusername/pendo_essence')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pendo_essence.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## STEP 8: .htaccess for public_html/

```apache
PassengerEnabled On
PassengerAppRoot /home/yourusername/pendo_essence
PassengerAppType wsgi
PassengerStartupFile pendo_essence/wsgi.py
PassengerPythonPath /home/yourusername/virtualenv/pendo_essence/3.11/bin/python3.11

<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ /passenger_wsgi.py/$1 [QSA,L]
</IfModule>
```

## STEP 9: Admin Setup

1. Visit: https://yourdomain.com/admin/
2. Login with your superuser credentials
3. Go to **Site Settings** and fill in:
   - Phone number
   - WhatsApp number
   - Social media links
   - Delivery settings
4. Add product images through **Products**

## STEP 10: Final Checklist

- [ ] DEBUG = False in settings.py
- [ ] SECRET_KEY changed
- [ ] ALLOWED_HOSTS set correctly
- [ ] Static files collected
- [ ] Database migrated
- [ ] Admin user created
- [ ] Site settings configured
- [ ] At least 1 product added with image
- [ ] WhatsApp number set

## TROUBLESHOOTING

**500 Error**: Check error logs in cPanel → Logs → Error Log
**Static files not loading**: Run `python manage.py collectstatic`
**Images not showing**: Check MEDIA_ROOT and MEDIA_URL in settings
**Database errors**: Run `python manage.py migrate`

## SUPPORT

