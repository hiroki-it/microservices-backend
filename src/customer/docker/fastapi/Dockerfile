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

RUN pip3 install \
     --upgrade pip \
     -r requirements.txt

#===================
# development Stage
#===================
FROM base as development
LABEL mantainer=${LABEL}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

#===================
# Production Stage
#===================
FROM base as production
LABEL mantainer=${LABEL}

COPY ./ /var/www/customer/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
