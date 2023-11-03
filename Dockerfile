FROM python:3.11.3-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN mkdir app

WORKDIR app
COPY . .
RUN pip install -r req.txt

ENTRYPOINT ["bash","django-start.sh"]