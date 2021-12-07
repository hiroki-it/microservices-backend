#===================
# Global ARG
#===================
ARG PHP_FPM_VERSION=8.0.13
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Base Stage
#===================
FROM php:${PHP_FPM_VERSION}-fpm as base

RUN apt-get update -y \
  && apt-get install -y \
      git \
      vim \
      unzip \
      zip \
  && docker-php-ext-install \
      bcmath \
      pdo_mysql \
  # キャッシュ削除
  && apt-get clean

COPY --from=composer:1.10.23 /usr/bin/composer /usr/bin/composer

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

COPY ./ /var/www/helloworld-service-with-php/
