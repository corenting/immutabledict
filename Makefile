PYTHON=poetry run

.PHONY: format
format:
	$(PYTHON) black immutabledict tests
	$(PYTHON) isort immutabledict tests

.PHONY: style
style:
	$(PYTHON) black --check immutabledict tests
	$(PYTHON) isort --check-only  immutabledict tests
	$(PYTHON) mypy -- immutabledict
	$(PYTHON) pflake8 immutabledict tests

.PHONY: test
test:
	$(PYTHON) pytest tests --cov=immutabledict --cov-report=xml
