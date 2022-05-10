# Static and Media Files

## Serving Media Files
You'll have to set a media root and media url for Django to use

In settings.py:
````python
MEDIA_URL = '/media'
MEDIA_ROOT = '/path/to/media'
````

MEDIA_URL is the URL to navigate to that contains the media files

MEDIA_ROOT is the absolute path to the directory containing the media files

You'll also have to add the URL path to URLPATTERNS

In urls.py:
````python
from django.conf import settings

urlpatterns = [
    ...,
    ...,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
````

This lets you access media files using a URL to the media like `localhost:8000/media/file.mp3`

You'll have to add the Django context processor for media files to access the URL in the templates

in settings.py:
````python
TEMPLATES = [
    {
        'OPTIONs': {
            'context_processors': [
                'django.template.context_processors.media',
            ]
        }
    }
]
````

Once you have the context processor, you can access the MEDIA_URL in templates

index.html
````html
{{ MEDIA_URL }}
{{ MEDIA_URL }}/filename.mp3
````
Will serve the media file from the URL

- - - -

# Deployment
## Serving Static and Media Files in Production
For production you'll have to setup the server to serve media and static files

Apache:
````bash
<Directory /path/to/media>
Require all granted
</Directory>
````

NGINX:
````bash
location /media/{
    autoindex on;
    alias /path/to/media/;
}
````
*Make sure to reload Apache2 or NGINX after changing config files!*
It would be the same for static.

## Setting up HTTPS and SSL
Once you have a working server that serves the Django site over HTTPS, you will need to add some settings to settings.py

````python
# HTTPS / SSL Settings
if DEBUG == False:
    CSRF_COOKIE_SECURE = True   # Encrypts CSRF Token
    SESSION_COOKIE_SECURE = True    # Encrypts cookies
    SECURE_SSL_REDIRECT = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"  # Protects against attacks
    CSRF_TRUSTED_ORIGINS = ['https://lupobudgets.co.uk']

    # Secure HSTS Settings
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000  # 1 Year in seconds
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
````