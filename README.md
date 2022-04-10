# microservices-backend

## 概要

マイクロサービスアーキテクチャのアプリケーションのバックエンド領域を管理するリポジトリ．

GitOpsの **[ベストプラクティス](https://blog.argoproj.io/5-gitops-best-practices-d95cb0cbe9ff)** に則って，マニフェストファイルは **[microservices-manifestsリポジトリ](https://github.com/hiroki-it/microservices-manifests)** で管理しています．

現状，フロントエンド領域のリポジトリは用意しておりません．

<br>

## 開発運用シナリオ

SWEチームが以下のようなシナリオで開発運用していること，を想定しながら練習しております．

1. 境界付けられたコンテキストごとにマイクロサービスが存在しており，それぞれのマイクロサービスは独立したSWEチームによって開発されている．各マイクロサービスにて，SWEはDocker Composeを用いて開発しており，Kubernetesのマニフェストファイルを仕様を知らなくても良い．全てのマイクロサービスはモノリポジトリで管理されている．
2. SWEチームのいずれかは，マイクロサービスのソースコードを変更し，プルリクを作成する．またGitFlowを経て変更がmainブランチにマージされる．この時，異なるマイクロサービスの変更が同時にマージされることはない．
3. 本リポジトリ上のCircleCIは，変更されたマイクロサービスを検知し，該当のマイクロサービスのイメージをビルドする．また，AWS ECRにプッシュする．
4. CircleCIは，**[microservices-manifestsリポジトリ](https://github.com/hiroki-it/microservices-manifests)** をプルし，releaseブランチをチェックアウトする．さらに，HelmのValuesファイルのイメージのハッシュ値の上書きし，コミット&プッシュする． その後，Valuesファイルを変更したプルリクを自動作成する．
5. **[microservices-manifestsリポジトリ](https://github.com/hiroki-it/microservices-manifests)** 上のGitHub Actionsは，releaseブランチのプッシュを検知する．この時，HelmがValuesファイルを基にしてマニフェストファイルを自動生成し，これをプルリク上にプッシュする．最後に，HelmのチャートがAWS ECRにプッシュされる．
6. SWEチーム/SREチームのリリース責任者が，プルリクをmainブランチにマージする．
7. AWS EKS上で稼働するArgoCDがmainブランチの変更を検知し，AWS ECRからチャートをプルする．

参考：

- マイクロサービスアーキテクチャ: https://hiroki-it.github.io/tech-notebook-mkdocs/software/software_application_architecture_backend_microservices.html
- 境界付けられたコンテキスト: https://hiroki-it.github.io/tech-notebook-mkdocs/software/software_application_architecture_backend_domain_driven_design.html

<br>

## ディレクトリ構成

```bash
.
├── ops # CIで用いるスクリプト
└── src # マイクロサービス
```

<br>

## 使用技術

### マイクロサービスの一覧

バックエンド領域を構成するマイクロサービスの一覧です．

マイクロサービスは，境界付けられたコンテキストに基づいて分割するようにしております．

| マイクロサービス名                                                                                         | 言語     | フレームワーク | プロキシコンテナ    | 境界付けられたコンテキストの説明  |
|---------------------------------------------------------------------------------------------------|--------|---------|-------------|-------------------|
| [accountサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/account)           | Go     | Gin     | Envoy       | 会計業務ドメインを解決します．   |
| [customerサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/customer)         | Python | FastAPI | Envoy       | 顧客管理業務ドメインを解決します． |
| [orchestratorサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/orchestrator) | Python | FastAPI | Envoy       | トランザクションの項目を参照．   |
| [orderサービス](https://github.com/hiroki-it/microservices-backend/tree/main/src/order)               | PHP    | Lumen   | Nginx，Envoy | 受注業務ドメインを解決します．   |

### 開発ツール

開発環境でのみ使用するツールの一覧です．

| 役割         | ツール                            | 導入の状況          |
|------------|--------------------------------|----------------|
| メトリクスの可視化  | Prometheus，Kiali               | ⭕              |
| ログの可視化     | FluentBit，ElasticSearch，Kibana | coming soon... |
| 分散トレースの可視化 | Jaeger                    　　　  | ⭕              |
| ロードテスト     | Fortio                         | ⭕              |

### CI/CD

CI/CDを構成するツールの一覧です．

| 役割   | ツール      | 導入の状況          |
|------|----------|----------------|
| CI（本番環境）   | CircleCI | ⭕ |
| CD（本番環境）    | ArgoCD   | **[microservices-manifestsリポジトリ](https://github.com/hiroki-it/microservices-manifests)** を参照 |

<br>

### 補足

#### ▼ マイクロサービス間通信の方式

リクエストリプライ方式を採用し，『API Gateway → マイクロサービスA ⇄ マイクロサービスB』という簡単な構成を想定しております．

#### ▼ トランザクション

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


## 環境構築

各マイクロサービスのREADMEをご参照ください．
