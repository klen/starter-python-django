# target: help - Display callable targets
.PHONY: help
help:
	@egrep "^# target:" [Mm]akefile | sed -e 's/^# target: //g' | sort


# target: clean - Clean project
.PHONY: clean
clean:
	@rm -rf build dist docs/_build
	@rm -f *.py[co]
	@rm -f *.orig
	@rm -f */*.py[co]
	@rm -f */*.orig

.PHONY: register
# target: register - Register module on PyPi
register:
	@python setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload:
	@python setup.py sdist upload || echo 'Upload already'
