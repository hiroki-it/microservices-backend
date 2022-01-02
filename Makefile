POD=

minikube-start:
	# Istioを使用するために必要な最低限のスペック
	minikube config set cpus 4
	minikube config set memory 16384
	# ノードの構築
	minikube delete
	minikube start --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"
	# イングレスの有効化
	minikube addons enable ingress
	# メトリクスの有効化
	minikube addons enable metrics-server
	# dockerクライアントの向き先の変更
	minikube docker-env
	# 手動で実行
	# eval $(minikube -p minikube docker-env)

kubectl-proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 

kubectl-exec:
	kubectl exec -it ${POD} -- bash

enable-istio:
	istioctl install -f ./istio-manifests/operator.yml -y
	istioctl verify-install
	kubectl apply -f ./istio-manifests/gateway.yml
	kubectl apply -f ./istio-manifests/virtualService.yml
