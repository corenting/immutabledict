PYTHON=poetry run

.PHONY: format
format:
	$(PYTHON) ruff format immutabledict tests
	$(PYTHON) ruff check --fix immutabledict tests

.PHONY: style
style:
	$(PYTHON) ruff format --check immutabledict tests
	$(PYTHON) ruff check immutabledict tests
	$(PYTHON) pyright -- immutabledict tests
	@if $(PYTHON) python -c "import pyrefly" 2>/dev/null; then $(PYTHON) pyrefly check immutabledict tests; else echo "pyrefly not available, skipping"; fi

.PHONY: test
test:
	$(PYTHON) pytest tests --cov=immutabledict --cov-report=xml

.PHONY: build-doc
build-doc:
	$(PYTHON) sphinx-build -M html docs docs/build
