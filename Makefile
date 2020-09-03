install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	#poetry run pytest --cov==gendiff
	poetry run coverage run -m pytest

publish: lint test
	@poetry publish -r test_pypi --build
