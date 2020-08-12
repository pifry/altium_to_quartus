PHONY: test
test:
	cd altium_to_quartus && python -m unittest -v

PHONY: lint
lint:
	pylint altium_to_quartus