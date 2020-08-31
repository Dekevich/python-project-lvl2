install:
	poetry install

publish:
	@poetry publish -r test_pypi --build
