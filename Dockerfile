FROM python:3.8-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
