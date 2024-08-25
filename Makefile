VERBOSE=-vv

linting:
	poetry run mypy .
	poetry run black .

unit-tests:
	poetry run pytest . ${VERBOSE}

format:
	poetry run black .

check-poetry:
	poetry run python ./pre-commit-scripts/check-poetry.py

bump-version:
	poetry run python ./pre-commit-scripts/bump-version.py

bump-version-sh:
	poetry run ./pre-commit-scripts/bump-version.sh

package:
	poetry run python setup.py sdist bdist_wheel
