FROM node:22.3.0
RUN apt-get update -qq && apt-get install -y vim gosu

RUN mkdir /frontend
WORKDIR /frontend

COPY . /frontend

ADD entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT [ "entrypoint.sh" ]