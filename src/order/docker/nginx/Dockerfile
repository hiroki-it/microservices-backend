#===================
# Global ARG
#===================
ARG NGINX_VERSION=1.19
ARG LABEL="Hiroki <hasegawafeedshop@gmail.com>"

#===================
# Build Stage
#===================
FROM nginx:${NGINX_VERSION} as build

WORKDIR /var/www/order

RUN apt-get update -y \
  && apt-get install -y \
      curl \
      vim \
  # キャッシュ削除
  && apt-get clean

#===================
# Dev Stage
#===================
FROM build as dev
LABEL mantainer=${LABEL}

COPY ./docker/nginx/development.nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

#===================
# Prd Stage
#===================
FROM build as prd
LABEL mantainer=${LABEL}

COPY ./docker/nginx/production.nginx.conf /etc/nginx/nginx.conf

COPY ./ /var/www/order/

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
