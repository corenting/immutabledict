PYTHON=poetry run

.PHONY: format
format:
	$(PYTHON) ruff format immutabledict tests
	$(PYTHON) ruff --fix immutabledict tests

.PHONY: style
style:
	$(PYTHON) ruff format --check immutabledict tests
	$(PYTHON) ruff immutabledict tests
	$(PYTHON) mypy -- immutabledict tests

.PHONY: test
test:
	$(PYTHON) pytest tests --cov=immutabledict --cov-report=xml

.PHONY: build-doc
build-doc:
	$(PYTHON) sphinx-build -M html docs docs/build
