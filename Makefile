install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	coverage run --source=gendiff -m pytest -vv
	coverage xml

publish: lint test
	@poetry publish -r test_pypi --build
