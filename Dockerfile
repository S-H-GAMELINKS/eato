FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update && apt-get install postgresql postgresql-contrib -y
RUN pip install -r requirements.txt
ADD . /code/
