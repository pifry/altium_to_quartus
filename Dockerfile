FROM python:3.8

WORKDIR /usr/src/app

COPY requirements/development.txt ./
RUN pip install --no-cache-dir -r development.txt