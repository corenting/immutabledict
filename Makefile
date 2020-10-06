PYTHON=poetry run

.PHONY: format
.SILENT: format
format:
	$(PYTHON) black .
	$(PYTHON) isort .

.PHONY: format-check
.SILENT: style
style:
	$(PYTHON) black --check .
	$(PYTHON) isort --check-only  .

.PHONY: test
.SILENT: test
test:
	$(PYTHON) pytest tests --cov=immutabledict