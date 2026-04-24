"""
Pendo Essence - Django Settings
Render.com deployment ready
"""
# render Email: info@nalalahouse.com

import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ─── SECURITY ────────────────────────────────────────────────────────────────
SECRET_KEY = os.environ.get('SECRET_KEY', 'pendo-essence-change-this-in-production')

DEBUG = 'False'

ALLOWED_HOSTS = [
    '*',
    'localhost',
    '127.0.0.1',
    'pendoessence.co.tz',
    'www.pendoessence.co.tz',
    '.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://pendoessence.co.tz',
    'https://www.pendoessence.co.tz',
]

# ─── APPS ────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'pyuploadcare.dj',
    'store',
]

JAMIITEK_API_URL = "https://jamiitek.com/api/site-status/"
JAMIITEK_API_KEY = "e3RgG035SeV-x1sZEtN9HFx3WqAr43pvPTeSMzk7gTFZlMArf6pH_6y6mnwK2Egg"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'jamiitek_middleware.JamiiTekStatusMiddleware',
]

ROOT_URLCONF = 'pendo_essence.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.cart_processor',
                'store.context_processors.site_settings_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'pendo_essence.wsgi.application'

# ─── DATABASE ────────────────────────────────────────────────────────────────
# Render inatoa DATABASE_URL automatically kama unatumia Render PostgreSQL
# Au tumia Supabase kama ilivyo kwenye project yako
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'postgres'),
            'USER': os.environ.get('DB_USER', 'postgres.wuuiurtgqixcwlqxiikv'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'NyumbaChap@123'),
            'HOST': os.environ.get('DB_HOST', 'aws-1-eu-west-1.pooler.supabase.com'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }

# ─── AUTH ────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── I18N ────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_TZ = True

# ─── STATIC FILES ────────────────────────────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ─── UPLOADCARE ──────────────────────────────────────────────────────────────
UPLOADCARE = {
    'pub_key': os.environ.get('UPLOADCARE_PUBLIC_KEY', '4c3ba9de492e0e0eaddc'),
    'secret': os.environ.get('UPLOADCARE_SECRET_KEY', '28410d13b3cb1098451e'),
}

# ─── EMAIL ───────────────────────────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'info@pendoessence.co.tz')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'Pendo Essence <info@pendoessence.co.tz>'

# ─── SESSION ─────────────────────────────────────────────────────────────────
SESSION_COOKIE_AGE = 86400 * 30
SESSION_SAVE_EVERY_REQUEST = True

# ─── LOGIN ───────────────────────────────────────────────────────────────────
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
