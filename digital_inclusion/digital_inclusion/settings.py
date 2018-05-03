"""
Django settings for digital_inclusion project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET', '8a!*u9-u%^q96g@#si_v#q)t097r$i20pp1*g@wlg!+gx1p*0c')

# SECURITY WARNING: don't run with debug turned on in production!
if not os.environ.get('PROD', None):
    DEBUG = True

ALLOWED_HOSTS = ['django.local', 'django.dry', 'deca.nanoapp.io', 'resource.digitalatx.org', '172.21.0.2']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'digital_inclusion',
    'widget_tweaks',
    'phonenumber_field',
    'import_export',
    'formtools',
    'crispy_forms',
    'ckeditor',
    'main',
    'organization_management',
    'user_management',
    'flagging',
    'events',
    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digital_inclusion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'digital_inclusion/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digital_inclusion.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if os.environ.get('DATA_DB_HOST', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gonano',
            'USER': os.environ.get('DATA_DB_USER'),
            'PASSWORD': os.environ.get('DATA_DB_PASS'),
            'HOST': os.environ.get('DATA_DB_HOST'),
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PHONENUMBER_DEFAULT_REGION = 'US'

IMPORT_EXPORT_USE_TRANSACTIONS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/uploads/media/')
MEDIA_URL = '/media/'
AUTH_USER_MODEL = "user_management.User"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"

#Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_SMTP_HOST', 'smtp.gmail.com')
EMAIL_PORT = os.environ.get('EMAIL_SMTP_TLS_PORT', 465)
EMAIL_HOST_USER = os.environ.get('EMAIL_SMTP_USERNAME', 'evan.mosseri')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_SMTP_PASSWORD', 'rotterdam143')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_SMTP_FROM_EMAIL', "evan.mosseri@gmail.com")

# Custom Settings

GOOGLE_MAPS_JS_API_KEY = "AIzaSyD4Gkn1pvJSIDhIzZSh_zFqlwbp0NMByA0"
GOOGLE_MAPS_API_KEY = "AIzaSyCC5cUSznV06nmGOX2mdGACzdqNLBGiFxE"
GOOGLE_CALENDAR_API_KEY = "AIzaSyCoFMVlVvKypdsI24prKagic0TkS-6-QBA"
# GOOGLE_MAPS_JS_API_KEY = "AIzaSyCoFMVlVvKypdsI24prKagic0TkS-6-QBA"

GOOGLE_CALENDAR_CREDS = {
    "type": "service_account",
    "project_id": "ut-deca",
    "private_key_id": "59cf4aecac114c7fd1478225e1f6f5bf2a014a9b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDXn59fifRUqm2A"
                   "\n1PnEfjQItAmCaBc9HPoTrfeYuqFqWgdRMH8sQdHKls+Kb2P8ewJyyHFiRsDAAA2l\nxn4"
                   "/RmI2EyFshQpSv0LVxlgld3z86RIgMgMKjUwiBVOuxWPKo6+bo1ZEoXjTevSC"
                   "\n0fIvR6wA2Dgd4v5iWfniqZrQxK4giph2L4Hdg8/REGEh+Jhs7SvsMqD7uPfiTfqX\nBvvlIXs5dcvzO"
                   "+H9xafmZWhlbz28ep6wB3IzZvmWUjXf8dyrhQ6sc3fIvawI+lPK\nesnlyfBjT1h4G7ul6ytAhYRf8DAm/79eS0"
                   "/gI9XX3JE0llmLhzNM4qKGwVYif5nV\nAGgCdEmrAgMBAAECggEAZ1jbBuw0vvXWuVabBiplHzzHiAkDBmgilpcd4salAjf3"
                   "\nZNslQR2lA4BoJhaAqm18/W4EJlH6JayA3hF2xjYicX+W2BAmJAYG7zZ7Xi3YqtG9\nPdAqs"
                   "/6IXJAIDW8PhvsQerz9ZrSsGFTI6ADfnvivwNHhh7WaLqKoihK3oNN8EBzs\nBAu+EmurhS20vhJ80VZ8WEpC1"
                   "/TBEJRoGwMho4BAL4dNDcwveyNlVyLbbUqQSMSe\nlpP"
                   "/24Np11kiHS7OUq7r6wOYsWrEckEhD3QUfpqBYdUeoofZ7iklcdRG15fHcSVd"
                   "\nPcXMmJw4NDVBsBzFwmnXzfloyD5r7tl3kQruQr0UBQKBgQD67o0l9mjY1kI1wuYc\negVBh"
                   "+47ZhZcNvQC1V2mlVH6DQhU6jUntmEoekYWvAcFH+/efFiAs+OZDgMZL/mK\nd7eoS4joiyccjQ90+3lahIp7m/PwPhkDN"
                   "/UHt9kphFANsSFsVzXf88DvWNWAkc5A\nCaQ4LcwpOsXGoXHvKexp0Ui5hQKBgQDb+oI+UT5Lg/2Ou4Km4kP1eBx8Wn+0v3UZ"
                   "\n8BCgsF3/6gXAxDTsSK5mqrUuvQDqrPC6M7P59zl+2hn4l9KTK1IFqQ8Syab94+vr\nSybPlF9Ax50fvHtw3Hs83B47V"
                   "+f5vG+PacEHqrEPKzTV56HVOeTSL6Jmr3AlsjGk\nFDpW+K9FbwKBgQCFwtoc7XBQfk5HCEDP1z"
                   "+sAgC9SxsKRwTl6cUFQr2zNHVHhp2V\nMMQz5pIsFkkLs02TZOdsm/fsI6sFJyy3Yj/Vh4ZQp7TOpGcj7dVvqg2D/MsZOpDs"
                   "\nxUxps9ggKHbgBZcSgJ6oZfBn5gvRgGfYfQs8IzWcmMbKrk7ktY1fjv9cXQKBgQCR\n2+4GYhpbOh6jSKPeAgOrvMOulNc"
                   "+wwBjfXGZCriZWtQLuE2bKqoxOxm97uavtJI9\n9NBue0XtXbKAyjJ"
                   "/EOdnB20OORV4HWut7XvDgg8SxgjiJTj4Ycl5Vj7ZfHU9e3vB\nbQ7oBX83np9"
                   "/AgKlfqjB0YHucn97D0epExyH1IdrEwKBgDjPRyol/14qfgAjvkkS"
                   "\nfuALgK7R15Z0pRRlrpmFLlPvVWIGPFf72JDvUEmJhSXHICswGVgNnoTOfbXH+Jc4\nSh6JHLRUerkaYOh3L5AKqkTeguoCz"
                   "/Ieoa5juZxwjbgIKEkx+baN6BvRJPllEFie\nYhwJqRybnmEj796HIOJTiLHx\n-----END PRIVATE KEY-----\n",
    "client_email": "emosseri@ut-deca.iam.gserviceaccount.com",
    "client_id": "101847419379212501244",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/emosseri%40ut-deca.iam.gserviceaccount.com"
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
