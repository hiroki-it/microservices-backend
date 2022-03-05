# microservices-backend

## マイクロサービスアーキテクチャの構成

### アプリケーション

#### ■ 一覧

アプリケーションを構成するマイクロサービスの一覧です．

| マイクロサービス名                                                                                                 | 言語     | フレームワーク | プロキシコンテナ    | 境界付けられたコンテキストの説明  |
|-----------------------------------------------------------------------------------------------------------|--------|---------|-------------|-------------------|
| [accountサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/account)           | Go     | Gin     | Envoy       | 会計業務ドメインを解決します．   |
| [customerサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/customer)         | Python | FastAPI | Envoy       | 顧客管理業務ドメインを解決します． |
| [orchestratorサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/orchestrator) | Python | FastAPI | Envoy       | トランザクションの項目を参照．   |
| [orderサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/order)               | PHP    | Lumen   | Nginx，Envoy | 受注業務ドメインを解決します．   |


#### ■ マイクロサービス間通信の方式

リクエストリプライ方式を採用し，『API Gateway → マイクロサービスA ⇄ マイクロサービスB』という簡単な構成を想定しております．

#### ■ トランザクション

オーケストレーションベースのSagaパターンを採用する想定です．
[**orchestratorサービス**](https://github.com/hiroki-it/microservices-backend/tree/main/src/orchestrator) を用意し，これが各マイクロサービスの一連のローカルトランザクションを連続的に実行します．

```mermaid
%%{init:{'theme':'dark'}}%%
graph TD
    A([Internet]) --> B[API Gateway]
    B             ----> C[customer-service]
    B             --> E[orchestrator-service]
    C             --> D[(DB)]
    E             --> F[Queue]
    F             --> G[order-service]
    F             --> I[account-service]
    G             --> H[(DB)]
    I             --> J[(DB)]
```

#### ■ 参考

マイクロサービスアーキテクチャについては，以下に整理しております．
<br>参考：https://hiroki-it.github.io/tech-notebook-mkdocs/software/software_application_architecture_backend_microservices.html

また，境界づけられたコンテキストについては，以下に整理しております．
<br>参考：https://hiroki-it.github.io/tech-notebook-mkdocs/software/software_application_architecture_backend_domain_driven_design.html

### インフラ

#### ■ 一覧

インフラを構成するツールの一覧です．
ソースコードは **[別のリポジトリ](https://github.com/hiroki-it/microservices-infrastructure)** で管理しています

| 役割              | ツール                 | 導入の状況          |
|-----------------|---------------------|----------------|
| 仮想化             | Docker              | ◯              |
| コンテナオーケストレーション  | Kubernetes          | ◯              |
| マイクロサービス間通信の管理  | Istio，IstioOperator | ◯              |
| プロキシコンテナ        | Envoy，Nginx         | ◯              |
| テンプレート管理        | Helm                | coming soon... |
| API Gateway     | AWS API Gateway     | coming soon... |
| Kubernetesの実行環境 | AWS EKS             | coming soon... |

#### ■ マイクロサービス間通信の管理

マイクロサービス間通信の管理方法は，リクエストリプライ方式に基づくサービスメッシュを実現するIstioを採用します．
プロキシコンテナはEnvoyとしますが，インバウンド通信をFastCGIプロトコルでルーティングする場合にNginxも用いる想定です．
この時，HTTPプロトコルによる同期通信を行い，gRPCプロトコルは用いない想定です．
ちなみに，イベント駆動方式を採用している場合は，イベントメッシュになります．

参考：https://www.redhat.com/ja/topics/integration/what-is-an-event-mesh

### デバッグツール

開発環境でのみ使用するデバッグツールの一覧です．

| 役割               | ツール                             | 導入の状況      |
| ----------------- | --------------------------------- | --------------- |
| メトリクスの可視化     | Prometheus，Kiali               | ◯               |
| ログの可視化          | FluentBit，ElasticSearch，Kibana | coming soon...  |
| 分散トレースの可視化   | Jaeger                    　　　 | ◯               |
| ロードテスト         | Fortio                           | ◯               |

### CI/CD

CI/CDを構成するツールの一覧です．

| 役割                         | ツール               | 導入の状況      |
| ---------------------------- | -------------------- | --------------- |
| CI/CD（開発環境）              | Skaffold             | ◯               |
| CI（本番環境）                 | CircleCI               | coming soon... |
| CD（本番環境）                  | ArgoCD               | coming soon... |

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
