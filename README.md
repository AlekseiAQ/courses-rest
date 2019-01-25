# Courses REST

## Usage

1. `docker-compose up --build`
2. `docker-compose run web python loaddata core\fixtures\initial.json`

## Notes

1. Create superuser `docker-compose run web python manage.py createsuperuser` or `python manage.py createsuperuser`
2. Login here: [http://127.0.0.1:8000/drf/api/login/](http://127.0.0.1:8000/drf/api/login/)
3. Try API here: [http://127.0.0.1:8000/api/v1/doc](http://127.0.0.1:8000/api/v1/doc)
