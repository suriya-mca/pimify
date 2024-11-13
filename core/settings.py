from decouple import config
from pathlib import Path, os
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "*"]

LOCAL_APPS = [
    'api',
]

THIRD_PARTY_APPS = [
    'import_export',
    'image_uploader_widget',
    'login_history',
]

THIRD_PARTY_ADMIN_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
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
        "DIRS": [BASE_DIR / "templates"],
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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "data/db.sqlite3",
        "OPTIONS": {
            "init_command": "PRAGMA journal_mode=WAL;",
            "init_command": "PRAGMA synchronous = NORMAL;",
        },
    }
}
# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql',
#         "NAME": config("DB_NAME"),
#         "USER": config("DB_USER"),
#         "PASSWORD": config("DB_PASSWORD"),
#         "HOST": config("DB_HOST"),
#         "PORT": config("DB_PORT"),
#     }
# }

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

STATIC_ROOT = os.path.join(BASE_DIR ,'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_src')]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

UNFOLD = {
    "SITE_TITLE": "Pimify",
    "SITE_HEADER": "Pimify",
    "SITE_SYMBOL": "package",
    "THEME": "dark",
    "DASHBOARD_CALLBACK": "api.views.dashboard_callback",
    "STYLES": [
        lambda request: static("admin_dashboard/css/styles.css"),
    ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "255 250 240",
            "100": "255 238 204",
            "200": "254 215 170",
            "300": "253 186 114",
            "400": "251 146 60",
            "500": "245 121 0",
            "600": "220 98 10",
            "700": "184 79 18",
            "800": "140 62 25",
            "900": "104 47 24",
            "950": "66 28 20"
        },
    },
    "SIDEBAR": {
        "show_search": True,  
        "show_all_applications": False, 
        "navigation": [
            {
                "separator": False, 
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "home", 
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_staff,
                    },
                ],
            },
            {
                "title": _("Product Management"),
                "separator": False, 
                "collapsible": False,
                "items": [
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
                "separator": False, 
                "collapsible": False, 
                "items": [
                    {
                        "title": _("Suppliers"),
                        "icon": "local_shipping", 
                        "link": reverse_lazy("admin:api_supplier_changelist"),
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
                    {
                        "title": _("Product Suppliers"),
                        "icon": "compare_arrows",  
                        "link": reverse_lazy("admin:api_productsupplier_changelist"),
                        "permission": lambda request: request.user.is_staff,
                    },
                ],
            },
            # {
            #     "title": _("Authentication and Authorization"),
            #     "separator": True,
            #     "collapsible": False,
            #     "items": [
            #         {
            #             "title": _("Users"),
            #             "icon": "person", 
            #             "link": reverse_lazy("admin:auth_user_changelist"),
            #             "permission": lambda request: request.user.is_superuser,
            #         },
            #         {
            #             "title": _("Groups"),
            #             "icon": "group",
            #             "link": reverse_lazy("admin:auth_group_changelist"),
            #             "permission": lambda request: request.user.is_superuser,
            #         },
            #     ],
            # },
            {
                "title": _("Settings"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Organization"),
                        "icon": "settings", 
                        "link": reverse_lazy("admin:api_organization_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Users and Permissions"),
                        "icon": "manage_accounts", 
                        "link": reverse_lazy("admin:auth_user_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Logs"),
                        "icon": "monitoring", 
                        "link": reverse_lazy("admin:login_history_loginhistory_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],  
            },
        ],
    },
    "TABS": [
        {
            "models": [
                "api.organization",
                "api.apikey",
            ],
            "items": [
                {
                    "title": _("Organization Details"),
                    "link": reverse_lazy("admin:api_organization_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("API Keys"),
                    "link": reverse_lazy("admin:api_apikey_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
            ],
        },
        {
            "models": [
                "auth.user",
                "auth.group",
            ],
            "items": [
                {
                    "title": _("Users"),
                    "link": reverse_lazy("admin:auth_user_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Groups"),
                    "link": reverse_lazy("admin:auth_group_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                },
            ],
        },
    ],
}
