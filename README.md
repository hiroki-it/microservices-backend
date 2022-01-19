# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成



| マイクロサービス                                             | 言語   | フレームワーク | プロキシコンテナ     | 境界付けられたコンテキストの説明                             |
| ------------------------------------------------------------ | ------ | -------------- | -------------------- | -------------------------------------- |
| api-gateway（作成予定） | -     | -            |         -             | インバウンド通信を各マイクロサービスにルーティングします．Kubernetes外に配置するとし，AWS API Gatewayを使いたい（願望）． |
| [order-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/order-service) | PHP    | Lumen          | Nginx，Envoy                | 受注業務を実現します．                 |
| [payment-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/payment-service) | Go     | Gin            | Envoy | 会計業務を実現します．             |
| ***-service（作成予定）                                      | Python | Flask          | Envoy |                  -                      |                             |


<br>

## 環境構築

### minikubeの起動

```bash
$ make minikube-start

$ eval $(minikube -p minikube docker-env)
```

### デプロイ

#### ・Kubernetesの場合

```bash
$ make deploy-kubernetes
```

#### ・Istioの場合

```bash
$ make deploy-istio
```
