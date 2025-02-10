cd marvel
pip install django
pip install whitenoise
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver