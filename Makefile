start-minikube:
	# Istioを使用するために必要な最低限のスペック
	minikube config set cpus 4
	minikube config set memory 16384
	# ノードの構築
	minikube delete
	minikube start --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"
	# イングレスの有効化
	# minikube addons enable ingress
	# メトリクスの有効化
	minikube addons enable metrics-server
	# dockerクライアントの向き先の変更
	minikube docker-env
	eval $(shell minikube -p minikube docker-env)

kubectl-proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 

apply-k8s:
	skaffold run --force --no-prune=false --cache-artifacts=false

apply-k8s-with-pf:
	skaffold run --force --no-prune=false --cache-artifacts=false --port-forward

apply-istio:
	istioctl operator init
	istioctl install -y -f ./istio/operator/operator.yml
	kubectl apply -f ./istio/manifests
	istioctl verify-install

apply-istio-dashboard:
	kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/grafana.yaml
	kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/jaeger.yaml
	kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/prometheus.yaml

destroy-istio:
	istioctl x uninstall --purge -y

ISTIO_INGRESS=$(shell kubectl get service/istio-ingressgateway --namespace=istio-system -o jsonpath="{.status.loadBalancer.ingress[0].ip}")
load-test:
	# 同時に，make kubectl-proxy を実行しておくこと．
	# @see https://github.com/fortio/fortio#command-line-arguments
	docker run fortio/fortio load -c 1 -n 100 http://${ISTIO_INGRESS}/orders
