install:
	poetry install

lint:
	poetry run flake8 gendiff

publish: lint
	@poetry publish -r test_pypi --build
