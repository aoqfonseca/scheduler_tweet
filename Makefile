.PHONY: setup

setup:
	@pip install -r requirements.txt
	@python manage.py migrate


create_admin:
	@python manage.py createsuperuser

run:
	@python manage.py runserver 0.0.0.0:8000
