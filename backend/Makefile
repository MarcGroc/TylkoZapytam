default: format

format:
	poetry run black .
	poetry run isort . --profile=black

test:
	poetry run pytest . --cov-report term --cov=app
	poetry run coverage html -d tests/coverage_report
