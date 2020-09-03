install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov==gendiff

publish: lint test
	@poetry publish -r test_pypi --build
