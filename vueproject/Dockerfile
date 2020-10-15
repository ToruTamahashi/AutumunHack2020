FROM node:14.13
RUN apt-get update -qq && npm install -g @vue/cli
RUN mkdir /app
WORKDIR /app
COPY . /app