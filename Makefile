lint:
	black --check src
	isort --profile black --check-only src
	flake8 src

lint-fix:
	black src
	isort --profile black src

install-dependencies:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run-example:
	ENV=DEVELOPMENT python -m src.handlers.example

deploy-prod:
	sls deploy --stage=production

