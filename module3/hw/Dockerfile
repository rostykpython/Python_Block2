FROM python:3.7-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install pipenv
COPY Pipfile.lock ./
COPY Pipfile ./

RUN pipenv install --deploy --ignore-pipfile


COPY Test_package ./
ENTRYPOINT python main.py
