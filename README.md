# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成

| マイクロサービス            | 言語 | フレームワーク | 説明                                                         |
| --------------------------- | ---- | -------------- | ------------------------------------------------------------ |
| helloworld-service-with-php | PHP  | Lumen          |                                                              |
| helloworld-service-with-go  | Go   | Gin            |                                                              |
| database                    | -    | -              | MySQLを用いたデータベースです．各マイクロサービスが共有します．開発環境のみで使用します． |

<br>

## 環境構築

### minikubeの起動

```bash
$ make minikube-start

$ eval $(minikube -p minikube docker-env)
```

### kubernetesオブジェクトのビルド&デプロイ

```bash
$ skaffold run
```
