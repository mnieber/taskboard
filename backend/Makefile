runserver:
	python manage.py runserver 0.0.0.0:8000 --nostatic

create-db:
	env PGPASSWORD=dev psql -h postgres -d postgres -U postgres -c "CREATE USER django WITH CREATEDB PASSWORD 'dev';"
	env PGPASSWORD=dev psql -h postgres -d postgres -U django -c "CREATE DATABASE django;"
	env PGPASSWORD=dev psql -h postgres -d postgres -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE django TO django;"

pip-compile:
	pip-compile requirements.in -o requirements.txt
	pip-compile requirements.dev.in -o requirements.dev.txt

install:
	pip install -r requirements.dev.txt

setup: create-db pip-compile install
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py collectstatic