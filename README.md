# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成

| マイクロサービス            | 言語 | フレームワーク | 機能の説明                                                         |
| --------------------------- | ---- | -------------- | ------------------------------------------------------------ |
| [service-with-php](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/service-with-php) | PHP  | Lumen          |                                                              |
| [service-with-go](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/service-with-go) | Go   | Gin            |                                                              |
| service-with-python（作成予定） | Python | Flask | |

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
