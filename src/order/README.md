# orderサービス

## 環境構築

```bash
$ POD_NAME=<ポッド名>
$ kubectl exec -it -n microservices-with-kubernetes $POD_NAME -c lumen -- composer install COMPOSER_MEMORY_LIMIT=-1 --prefer-dist -vvv
```
