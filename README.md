ROBBY WAS HERE
brew install postgresql

pip install -r requirements.in && pip install -r dev-requirements.in

python manage.py makemigrations

python manage.py migrate

in ./backend do python manage.py celery

python manage.py createsuperuser
