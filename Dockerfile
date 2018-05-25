FROM python:3.6-alpine3.6

ENV GUNICORN_N_WORKERS 9
ENV GUNICORN_W_TIMEOUT 60
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
ENV ROUTER_URL=http://0.0.0.0:3000
ENV JWT_SECRET_KEY=test
ENV DB=postgresql://postgres:postgres@db

ADD . /app

WORKDIR /app

RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]