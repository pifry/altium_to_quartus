PHONY: test
test:
	cd altium_to_quartus && python -m unittest -v

PHONY: lint
lint:
	pylint altium_to_quartus

PHONY: test_contenerized
test_contenerized:
	docker-compose run atoq python -m unittest -v



