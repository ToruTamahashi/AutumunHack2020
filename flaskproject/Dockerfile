FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get -y install mariadb-client
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/