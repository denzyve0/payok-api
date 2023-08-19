VENV_NAME := venv
PYTHON := $(VENV_NAME)/Scripts/python

mkvenv:
	virtualenv $(VENV_NAME)
	$(PYTHON) -m pip install -r requirements.txt

clean:
	find . -name "*.pyc" -exec rm --force {} +
	find . -name "*.pyo" -exec rm --force {} +
	find . -name "*~" -exec rm --force  {} +
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

tag:
	PAYOKAPI_VERSION := $(shell $(PYTHON) -c "import payokapi;print(payokapi.__version__)")
	echo "Add tag: '$(PAYOKAPI_VERSION)'"
	git tag v$(PAYOKAPI_VERSION)

build:
	$(PYTHON) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

release:
	PAYOKAPI_VERSION := $(shell $(PYTHON) -c "import payokapi;print(payokapi.__version__)")
	make clean
	make tag
	make build
	@echo "Released payokapi $(PAYOKAPI_VERSION)"

full-release:
	make release
	make upload


make install:
	$(PYTHON) setup.py install
