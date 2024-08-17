linting:
	poetry run mypy .
	poetry run black .

unit-tests:
	poetry run pytest .

format:
	poetry run black .