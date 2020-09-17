FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements-dev.txt /app/
RUN pip install -r requirements-dev.txt
COPY . /app/
