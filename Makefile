minikube-start:
	minikube delete
	minikube start --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"
	minikube docker-env

kubectl-proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 
