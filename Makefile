default: format

format:
	black backend
	isort backend --profile black
	black deployment
	isort deployment --profile black

# below are not implemented yet
build-backend:
	docker build . -f backend/Dockerfile -t backend

build-fronted:
	docker build . -f frontend/Dockerfile -t frontend

build-task-runner:
	docker build . -f task_runner/Dockerfile -t task-runner


docker-compose:
	docker compose -f docker-compose.development.yml rm -s -v -f
	docker compose -f docker-compose.development.yml up --build

run-local:
	python backend/manage.py runserver
	cd frontend && npm start

tests:
	python backend/manage.py test