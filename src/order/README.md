# orderサービス

## 環境構築

```bash
$ docker-compose up -d

$ docker-compose exec app bash

# パッケージをインストールする．
[root@order-app:/var/www/order] $ composer install COMPOSER_MEMORY_LIMIT=-1 --prefer-dist -vvv

# lumenがstorageディレクトリにアクセスできるようにする．
# @see https://laracasts.com/discuss/channels/laravel/permission-denied-on-storagelogslaravellog
[root@order-app:/var/www/order] $ chmod -R 777 /var/www/order/storage

# テストデータをDBに挿入する．
[root@order-app:/var/www/order] $ php artisan migrate
```
