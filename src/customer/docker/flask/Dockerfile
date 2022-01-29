#===================
# Global ARG
#===================
ARG PYTHON_VERSION=3.10
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Base Stage
#===================
FROM python:${PYTHON_VERSION}-slim as base

#===================
# development Stage
#===================
FROM base as development
LABEL mantainer=${LABEL}

#===================
# Production Stage
#===================
FROM base as production
LABEL mantainer=${LABEL}

COPY ./ /var/www/customer/
