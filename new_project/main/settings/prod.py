from os import environ


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = []
origin = environ.get('AIPLATFORM_ORIGIN')
if origin:
    CSRF_TRUSTED_ORIGINS.append(origin)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'NAME': environ.get('AIPLATFORM_DB_NAME', 'new_project'),
        'USER': environ.get('AIPLATFORM_DB_USER', 'root'),
        'PASSWORD': environ.get('AIPLATFORM_DB_PASSWORD', ''),
        'HOST': environ.get('AIPLATFORM_DB_HOST', 'localhost'),
        'PORT': environ.get('AIPLATFORM_DB_PORT', '3306'),
    }
}
