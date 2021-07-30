release: python manage.py makemigrations python manage.py migrate
web: gunicorn auth_system.wsgi --log-file -