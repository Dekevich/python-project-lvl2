install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest -vv
	poetry run coverage xml

publish: lint test
	@poetry publish -r test_pypi --build
