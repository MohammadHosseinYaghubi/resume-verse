up:
	docker compose up --build

down:
	docker compose down

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

worker:
	celery -A config worker --loglevel=info

beat:
	celery -A config beat --loglevel=info

flower:
	celery -A config flower --port=5555

shell:
	python manage.py shell

createsuperuser:
	python manage.py createsuperuser