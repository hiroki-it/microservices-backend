POD=

minikube-start:
	# ノードの構築
	minikube delete
	minikube start --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"
	# イングレスの有効化
	minikube addons enable ingress
	minikube docker-env

kubectl-proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 

kubectl-exec:
	kubectl exec -it ${POD} -- bash

kubectl-port-forward-db:
	kubectl port-forward ${POD} 3308:3306
