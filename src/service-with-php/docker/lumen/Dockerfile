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
  # Lumen
  && apt-get install -y \
      git \
      vim \
      unzip \
      zip \
  && docker-php-ext-install \
      bcmath \
      pdo_mysql \
  # gRPC
  && apt-get install -y \
      zlib1g-dev \
  && pecl install grpc-1.42.0
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

COPY ./ /var/www/service-with-php/
