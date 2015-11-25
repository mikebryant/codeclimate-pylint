FROM python:2-onbuild

MAINTAINER Mike Bryant <mike@mikebryant.me.uk>

ADD engine.json /

RUN useradd -u 9000 -r -s /bin/false app
USER app
VOLUME /code
WORKDIR /code

ENV PYTHONPATH /usr/src/app

CMD [ "/usr/src/app/run.sh" ]
