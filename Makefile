start:
	minikube delete
	minikube start --driver=hyperkit --mount=true --mount-string="${HOME}/projects/hiroki-it/microservices-with-kubernetes:/data"

docker-compose-hswg:
	docker-compose -f ./src/helloworld-service-with-go/docker-compose.yml build

docker-compose-hswp:
	docker-compose -f ./src/helloworld-service-with-php/docker-compose.yml build

proxy:
	kubectl proxy --address=0.0.0.0 --accept-hosts='.*' 
