# From https://devcenter.heroku.com/articles/django-assets on 9/22/15
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)