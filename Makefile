PYTHON_CMD ?= python

requirements-dev.txt: requirements-dev.in
	pip-compile --no-emit-index-url --resolver=backtracking --output-file=requirements-dev.txt requirements-dev.in

create-virtualenv:
	python3.9 -m venv ./venv
	venv/bin/pip install -r requirements-dev.txt --no-dependencies

check-security:
	${PYTHON_CMD} -m bandit validator

lint-flake8:
	${PYTHON_CMD} -m flake8 --exclude=venv .

lint-black:
	${PYTHON_CMD} -m black --check --diff .

check-types:
	${PYTHON_CMD} -m mypy --ignore-missing-imports --follow-imports=silent --strict --allow-any-generics validator.py

run-unit-tests:
	${PYTHON_CMD} -m pytest -v --cov=validator --cov-report=term-missing tests/

all-checks: lint-black lint-flake8 check-types check-security run-unit-tests
