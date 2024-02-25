from pathlib import Path
import os
import environ

# Crear una instancia Env para poder acceder a las variables del sistema
env = environ.Env()
environ.Env.read_env()   

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Proteger la llave secreta desde una variable de entorno
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

# Administra los permisos de conexión del cliente hacia el backend (Dominios locales o externos permitidos)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV') # La declaramos en env


# Ahora hay que definir las aplicaciones instaladas 

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Configuramos nuestras apps del proyecto

PROJECTS_APPS = [
    
]

THIRD_PARTY_APPS = [
    'corsheaders', 
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'  # <-- aquí se debe de escribir así
]

# Terminar de configurar las apps del proyecto
INSTALLED_APPS = DJANGO_APPS + PROJECTS_APPS + THIRD_PARTY_APPS

# Configurar ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'autoParagraph': False
    }
}

# Definir dónde se van a cargar las imágenes
CKEDITOR_UPLOAD_PATH = '/media'

# Configurar el MIDDLEWARE para que corsheaders pueda hacer llamados a la API
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Configurar la migración de la BD de nuestro proyecto en Sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Código de lenguaje para español
LANGUAGE_CODE = 'es'

# Zona horaria para León, Guanajuato, México
TIME_ZONE = 'America/Mexico_City'

# Habilitar la internacionalización
USE_I18N = True

# Habilitar el uso de zonas horarias
USE_TZ = True

# Ruta donde Django recogerá los archivos estáticos tras ejecutar collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# URL que se utilizará para referirse a los archivos estáticos
STATIC_URL = '/static/'

# Ruta donde se guardarán los archivos multimedia subidos por los usuarios
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL que se utilizará para referirse a los archivos multimedia
MEDIA_URL = '/media/'

# Rutas donde Django buscará archivos estáticos adicionales, además de STATIC_ROOT
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist/statics')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de los permisos de Django-rest-framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly' # Tienes que estar logeado para poder editar
    ],
}

# Configurar de dónde pueden venir los llamados
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV') if DEBUG else env.list('CORS_ORIGIN_WHITELIST_DEPLOY')

# Configurar qué dominios puede hacer post / request
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')

# Configurar correo electrónico en modo de desarrollo
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Esto significa que los correos electrónicos que se envíen no se enviarán realmente, sino que se imprimirán 
# en la consola. Es una buena práctica para evitar enviar correos electrónicos accidentales durante el desarrollo

# Si estamos en modo de desarrollo, obtenemos la lista de hosts permitidos desde la variable de entorno 
# 'ALLOWED_HOSTS_DEV'

if DEBUG:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')
    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV')
    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')


# Si estamos en modo de producción, obtenemos la lista de hosts permitidos desde la variable de entorno 
# 'ALLOWED_HOSTS_PROD'
# También configuramos la base de datos usando la URL de la base de datos proporcionada en la variable de entorno 
# 'DATABASE_URL'

else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')
    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')
    DATABASES = {
        'default': env.db("DATABASE_URL")  # Esta línea se actualizará con la URL de la base de datos cuando 
        # despleguemos el proyecto
    }
    # Configuramos 'ATOMIC_REQUESTS' para evitar problemas con las transacciones de la base de datos
    DATABASES['default']['ATOMIC_REQUESTS'] = True

