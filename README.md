# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成

| マイクロサービス            | 言語 | フレームワーク | 機能の説明                                                         |
| --------------------------- | ---- | -------------- | ------------------------------------------------------------ |
| [order-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/order-service) | PHP  | Lumen          |                                                              |
| [payment-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/payment-service) | Go   | Gin            |                                                              |
| service-with-python（作成予定） | Python | Flask | |

<br>

## 環境構築

### minikubeの起動

```bash
$ make minikube-start

$ eval $(minikube -p minikube docker-env)
```

### ビルドとデプロイ

#### ・kubernetesの場合

```bash
$ make build-kubernetes
```

#### ・Istioの場合

```bash
$ make build-istio
```
