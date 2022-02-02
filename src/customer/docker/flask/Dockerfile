#===================
# Global ARG
#===================
ARG PYTHON_VERSION=3.10
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Base Stage
#===================
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /var/www/customer

ENV TZ Asia/Tokyo

COPY ./requirements.txt /var/www/customer/requirements.txt

RUN apt-get update -y \
  && apt-get install -y gcc \
  && pip install \
    --upgrade pip \
    -r requirements.txt

COPY ./docker/flask/uwsgi.ini /etc/wsgi/wsgi.ini

#===================
# development Stage
#===================
FROM base as development
LABEL mantainer=${LABEL}

CMD ["uwsgi", "--ini", "/etc/wsgi/wsgi.ini"]

#===================
# Production Stage
#===================
FROM base as production
LABEL mantainer=${LABEL}

COPY ./ /var/www/customer/

CMD ["uwsgi", "--ini", "/etc/wsgi/wsgi.ini"]
