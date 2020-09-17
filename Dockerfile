FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements-dev.txt /app/
RUN pip install -r requirements-dev.txt
COPY . /app/
