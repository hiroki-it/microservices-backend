#===================
# Global ARG
#===================
ARG PYTHON_VERSION=3.10
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Base Stage
#===================
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /var/www/orchestrator

ENV TZ Asia/Tokyo

COPY ./requirements.txt /var/www/orchestrator/requirements.txt

RUN pip3 install \
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

COPY ./ /var/www/orchestrator/

CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
