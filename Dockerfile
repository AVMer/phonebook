FROM python:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /phonebook
WORKDIR /phonebook
ADD . /phonebook/
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt