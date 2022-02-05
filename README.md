# microservices-with-kubernetes

## マイクロサービスアーキテクチャの構成

### アプリケーション

アプリケーションを構成するマイクロサービスの一覧です．

リクエストリプライ方式を採用し，『API Gateway → マイクロサービスA ⇄ マイクロサービスB』という簡単な構成を想定しております．

実装方法は以下に整理しております．

参考：https://hiroki-it.github.io/tech-notebook-mkdocs/software/software_application_architecture_backend_microservices.html


| マイクロサービス名                                          | 言語   | フレームワーク | プロキシコンテナ     | 境界付けられたコンテキストの説明                             |
| ------------------------------------------------------------ | ------ | -------------- | -------------------- | -------------------------------------- |
| [accountサービス](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/account) | Go     | Gin            | Envoy | 会計データ管理業務ドメインを解決します．             |
| [customerサービス](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/customer) | Python    | Flask          | Envoy                | 顧客データ管理業務ドメインを解決します．                 |
| [orderサービス](https://github.com/hiroki-it/microservices-with-kubernetes/tree/main/src/order) | PHP    | Lumen          | Nginx，Envoy                | 受注データ管理業務ドメインを解決します．                 |

### インフラ

インフラを構成するツールの一覧です．

マイクロサービス間の通信はHTTPプロトコルとし，gRPCプロトコルは用いない想定です．

プロキシコンテナはEnvoyとしますが，インバウンド通信をFastCGIプロトコルでルーティングする場合にNginxも用いる想定です．

| 役割                         | ツール               | 導入の状況      |
| ---------------------------- | -------------------- | --------------- |
| 仮想化              | Docker             | ◯               |
| コンテナオーケストレーション              | Kubernetes             | ◯               |
| サービスメッシュによるマイクロサービス間連携 | Istio，IstioOperator | ◯               |
| プロキシコンテナ | Envoy，Nginx | ◯               |
| テンプレート管理             | Helm                 | coming soon... |
| API Gateway                  | AWS API Gateway      | coming soon... |
| Kubernetesの実行環境                         | AWS EKS               | coming soon... |

### デバッグツール

開発環境でのみ使用するデバッグツールの一覧です．

| 役割               | ツール                       | 導入の状況      |
| ----------------- | --------------------------- | --------------- |
| テレメトリーの可視化  | Grafana，Jaeger，Prometheus | ◯               |
| ロードテスト         | Fortio                     | ◯               |

### CI/CD

CI/CDを構成するツールの一覧です．

| 役割                         | ツール               | 導入の状況      |
| ---------------------------- | -------------------- | --------------- |
| CI/CD（開発環境）              | Skaffold             | ◯               |
| CI（本番環境）                           | CircleCI               | coming soon... |
| CD（本番環境）                      | ArgoCD               | coming soon... |

<br>

## 環境構築

### Minikube

```bash
$ make minikube-start

$ eval $(minikube -p minikube docker-env)
```

### Kubernetes

```bash
$ make apply-k8s
```

### Istio

```bash
$ make apply-istio
```

### マイクロサービス

各マイクロサービスのREADMEをご参照ください．
