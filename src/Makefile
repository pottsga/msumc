create_env:
	mkdir env && python3 -m venv env

setup_dev:
	env/bin/pip install -e ".[dev]"

setup_prod:
	env/bin/pip install -e .

dev:
	env/bin/pserve development.ini --reload

start:
	env/bin/pserve development.ini --reload
