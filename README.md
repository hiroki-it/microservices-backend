# microservices-with-kubernetes

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
