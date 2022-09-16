.PHONY: dev clean init tests lint

lint:
	mypy dagster_hex
	isort dagster_hex
	black dagster_hex
	flake8 dagster_hex

tests:
	pytest -s -vv
