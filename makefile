.PHONY: all setup tests
# make >debug.log 2>&1
# git remote prune origin
ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
PTEST = venv/Scripts/pytest.exe
COVERAGE = venv/Scripts/coverage.exe
else
PYTHON = ./venv/bin/python
PTEST = ./venv/bin/pytest
COVERAGE = ./venv/bin/coverage
endif

SOURCE = source
TESTS = tests

FLAKE8 = $(PYTHON) -m flake8
PYLINT = $(PYTHON) -m pylint
PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered
PIP = $(PYTHON) -m pip install


all: tests

xxx:
	$(PYTHON) $(SOURCE)/main.py build/xxx.mp3 build/xxx.json

json:
	$(PYTHON) $(SOURCE)/main.py ~/task/xxx.mp3 ~/task/task.json

test:
	$(PTEST) -s $(TESTS)/test/$(T)

flake8:
	$(FLAKE8) $(TESTS)/test
	$(FLAKE8) $(SOURCE)

lint:
	$(PYLINT) $(TESTS)/test
	$(PYLINT) $(SOURCE)

pep257:
	$(PYTHON) -m pydocstyle $(TESTS)/test
	$(PYTHON) -m pydocstyle $(SOURCE)

tests: flake8 pep257 lint
	$(PYTEST) -m "not longrunning" --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt
	$(PIP) -r $(TESTS)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
