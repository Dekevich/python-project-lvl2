install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	#poetry run pytest --cov==gendiff
	poetry run coverage run --source=gendiff -m pytest
	poetry run coverage xml


publish: lint test
	@poetry publish -r test_pypi --build
