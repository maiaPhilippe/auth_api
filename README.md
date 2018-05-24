# Auth-api

Auth Api


## How to run

``` bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

# Enviromment variables

FLASK_APP=run.py

FLASK_ENV=development

ROUTER_URL=http://0.0.0.0:5000

JWT_SECRET_KEY=test

DB=postgresql://postgres:password@0.0.0.0:5432

``` bash
flask run --port=8500 --host=0.0.0.0
```