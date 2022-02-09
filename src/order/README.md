# orderサービス

## 環境構築

```bash
$ POD_NAME=<ポッド名>

$ kubectl exec \
    -it \
    -n microservices-with-k8s $POD_NAME \
    -c lumen \
    -- composer install COMPOSER_MEMORY_LIMIT=-1 --prefer-dist -vvv \
       # lumenがstorageディレクトリにアクセスできるようにする．
       # @see https://laracasts.com/discuss/channels/laravel/permission-denied-on-storagelogslaravellog
       && chmod -R 777 /var/www/order/storage
```
