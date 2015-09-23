from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
application = get_wsgi_application()        # From https://warehouse.python.org/project/whitenoise/
application = DjangoWhiteNoise(application) # From https://warehouse.python.org/project/whitenoise/