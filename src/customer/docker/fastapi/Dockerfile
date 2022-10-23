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

# mysqlclientのためにパッケージが必要．
# @see https://pypi.org/project/mysqlclient/
RUN apt-get update -y \
  && apt-get install -y \
      python3-dev \
      default-libmysqlclient-dev \
      build-essential \
  && pip3 install \
      --upgrade pip \
      -r requirements.txt

#===================
# Dev Stage
#===================
FROM base as dev
LABEL mantainer=${LABEL}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

#===================
# Prd Stage
#===================
FROM base as prd
LABEL mantainer=${LABEL}

COPY ./ /var/www/customer/

CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000" ]
