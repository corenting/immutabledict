PYTHON=poetry run

.PHONY: format
format:
	$(PYTHON) black immutabledict tests
	$(PYTHON) ruff --fix immutabledict tests

.PHONY: style
style:
	$(PYTHON) black --check immutabledict tests
	$(PYTHON) ruff immutabledict tests
	$(PYTHON) mypy -- immutabledict tests

.PHONY: test
test:
	$(PYTHON) pytest tests --cov=immutabledict --cov-report=xml
