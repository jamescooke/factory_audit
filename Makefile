.PHONY: venv install

# Update all requirements, test and lint project
all: install
	$(MAKE) -C factory_audit/ lint test

# Bootstrap virtualenv
venv:
	virtualenv venv --python=python3
	. venv/bin/activate && pip install -U pip

install:
	pip install -r requirements/base.txt
