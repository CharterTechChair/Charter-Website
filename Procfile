release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py syncdb
web: gunicorn charterclub.wsgi --log-file -
