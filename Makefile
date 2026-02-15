PYTHON=poetry run

.PHONY: format
format:
	$(PYTHON) ruff format immutabledict tests
	$(PYTHON) ruff check --fix immutabledict tests

.PHONY: style
style:
	$(PYTHON) ruff format --check immutabledict tests
	$(PYTHON) ruff check immutabledict tests
# 	check multiple type checkers
	$(PYTHON) pyright -- immutabledict tests
	$(PYTHON) pyrefly check immutabledict tests
	$(PYTHON) mypy immutabledict tests

.PHONY: test
test:
	$(PYTHON) pytest tests --cov=immutabledict --cov-report=xml

.PHONY: build-doc
build-doc:
	$(PYTHON) sphinx-build -M html docs docs/build
