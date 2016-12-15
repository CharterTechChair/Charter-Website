release: python manage.py syncdb --all
release: python manage.py migrate --fake
web: gunicorn charterclub.wsgi --log-file -
