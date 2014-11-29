.PHONY: setup
setup:
	@pip install -r requirements.txt
	@python manage.py migrate


create_admin:
	@python manage.py createsuperuser

.PHONY: statics
statics:
	@python manage.py collectstatic --noinput

.PHONY: deploy
deploy:
	@git push heroku master

run:
	@python manage.py runserver 0.0.0.0:8000

test:
	@python manage.py test
