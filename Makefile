PYTHON=poetry run

.PHONY: format
.SILENT: format
format:
	$(PYTHON) black immutabledict tests
	$(PYTHON) isort immutabledict tests

.PHONY: style
.SILENT: style
style:
	$(PYTHON) black --check immutabledict tests
	$(PYTHON) isort --check-only  immutabledict tests
	$(PYTHON) mypy -- immutabledict
	$(PYTHON) pflake8 immutabledict tests

.PHONY: test
.SILENT: test
test:
	$(PYTHON) pytest tests --cov=immutabledict
