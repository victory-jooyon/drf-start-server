init:
	python new_project/manage.py migrate

test:
	pytest new_project/

superuser:
	python new_project/manage.py createsuperuser

flush:
	mysql -u root -e 'DROP DATABASE new_project; CREATE DATABASE new_project CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;'

reset: flush init

run:
	python new_project/manage.py runserver

shell:
	python new_project/manage.py shell -i bpython

migrate:
	python new_project/manage.py makemigrations --merge
	python new_project/manage.py makemigrations
	python new_project/manage.py migrate

docker_build:
	git rev-parse HEAD > version
	docker build -t new_project-server .

docker_login:
	$$(aws ecr get-login --no-include-email)

docker_run: docker_down docker_build
	docker-compose up

docker_down:
	docker-compose down
