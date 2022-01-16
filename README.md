# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成



| マイクロサービス                                             | 言語   | フレームワーク | プロキシコンテナ     | 機能の説明                             |
| ------------------------------------------------------------ | ------ | -------------- | -------------------- | -------------------------------------- |
| api-gateway（作成予定） | -     | -            |         -             | インバウンド通信を各マイクロサービスにルーティングします．認証認可も実装するのは難易度高そう... |
| [order-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/order-service) | PHP    | Lumen          | Nginx                | 受注機能を提供します．                 |
| [payment-service](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/payment-service) | Go     | Gin            | Envoy（Istioによる） | 金額計算機能を提供します．             |
| ***-service（作成予定）                                      | Python | Flask          | Envoy（Istioによる） |                  -                      |                             |


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
