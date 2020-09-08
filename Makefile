install:
	poetry install

lint:
	poetry run flake8 --max-cognitive-complexity=7 diff_generator

test:
	poetry run coverage run --source=diff_generator -m pytest -vv
	poetry run coverage xml

publish: lint test
	@poetry publish -r test_pypi --build
