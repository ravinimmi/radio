# radio

### Prerequisites
- Postgres

### Setup
```
createdb radio
pip install -r requirements.txt
```

### Run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```