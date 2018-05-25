# Auth-api

Auth Api


## How to run

### Docker

``` bash
docker-compose build
docker-compose up -d
```

###virtualenv

``` bash
virtualenv -p python3 envname
source envname/bin/activate
pip3 install -r requirements.txt
```

# Enviromment variables

FLASK_APP=run.py

FLASK_ENV=development

ROUTER_URL=http://0.0.0.0:5000

JWT_SECRET_KEY=test

DB=postgresql://postgres:password@0.0.0.0:5432

``` bash
env FLASK_APP=run.py flask run --port=8500 --host=0.0.0.0
```

``` bash
virtualenv -p python3 envname
source envname/bin/activate
pip3 install -r requirements.txt
```

# Enviromment variables

FLASK_APP=run.py

FLASK_ENV=development

ROUTER_URL=http://0.0.0.0:5000

JWT_SECRET_KEY=test

DB=postgresql://postgres:password@0.0.0.0:5432

``` bash
env FLASK_APP=run.py flask run --port=8500 --host=0.0.0.0
```
