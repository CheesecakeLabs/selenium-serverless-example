## Requirements

1. Docker
1. Node.js, NPM
1. Python >= 3.7

## Setting up local environment:
1. run `npm install` to install the serverless framework
1. download your chromedriver from https://chromedriver.chromium.org/downloads and add to the project root folder
1. run `python -m venv venv` to initiate a python virtual environment
1. run `source ./venv/bin/activate` to activate the virtual enviroment
1. run `pip install -r requirements.txt` to install the production dependencies 
1. run `pip install -r requirements-dev.txt` to install the development dependencies


## Running Locally

1. Setup local environment following previous instructions
1. choose the handler you want to execute and run it following this pattern:
```bash
$ python -m src.handlers.example
```

## Scripts

You can check the scripts on the makefile


## Todo

- [ ] Setup CI/CD

## Important

Do not versionate .env files in real projects

## More information

1. https://github.com/umihico/docker-selenium-lambda
1. https://www.serverless.com/blog/container-support-for-lambda
