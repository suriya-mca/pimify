from decouple import config
from pathlib import Path, os
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "*"]

LOCAL_APPS = [
    'api',
]

THIRD_PARTY_APPS = [
    'import_export',
]

THIRD_PARTY_ADMIN_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.import_export',
]

INSTALLED_APPS = [
    *THIRD_PARTY_ADMIN_APPS,
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

ASGI_APPLICATION = "core.asgi.application"

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR ,'/static')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, '/static_src')]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

UNFOLD = {
    "SITE_TITLE": "Pimify",
    "SITE_HEADER": "Pimify",
    "SIDEBAR": {
        "show_search": True,  
        "show_all_applications": False, 
        "navigation": [
            {
                "title": _("Product Management"),
                "separator": True, 
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "home", 
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Currencies"),
                        "icon": "money", 
                        "link": reverse_lazy("admin:api_currency_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",  
                        "link": reverse_lazy("admin:api_category_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Products"),
                        "icon": "box",  
                        "link": reverse_lazy("admin:api_product_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                                        {
                        "title": _("Product Images"),
                        "icon": "image",  
                        "link": reverse_lazy("admin:api_productimage_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                ],
            },
            {
                "title": _("Stock Management"),
                "separator": True, 
                "collapsible": False, 
                "items": [
                    {
                        "title": _("Suppliers"),
                        "icon": "corporate_fare", 
                        "link": reverse_lazy("admin:api_supplier_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Product Suppliers"),
                        "icon": "compare_arrows",  
                        "link": reverse_lazy("admin:api_productsupplier_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Warehouses"),
                        "icon": "warehouse",  
                        "link": reverse_lazy("admin:api_warehouse_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                    {
                        "title": _("Stocks"),
                        "icon": "inventory", 
                        "link": reverse_lazy("admin:api_stock_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                ],
            },
            {
                "title": _("Authentication and Authorization"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person", 
                        "link": reverse_lazy("admin:auth_user_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Organization Details"),
                        "icon": "source_environment", 
                        "link": reverse_lazy("admin:api_organization_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
        ],
    },
}
