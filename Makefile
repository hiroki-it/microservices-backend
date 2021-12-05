minikube-start:
	minikube delete
	minikube start --docker-env --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"

kubectl-proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 
