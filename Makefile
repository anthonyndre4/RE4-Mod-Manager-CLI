linting:
	poetry run mypy .
	poetry run black .

unit-tests:
	poetry run pytest .

format:
	poetry run black .

check-poetry:
	poetry run python ./pre-commit-scripts/check-poetry.py
