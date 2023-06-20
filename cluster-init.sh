#!/bin/bash
kubectl delete --all all
minikube stop
minikube start
docker exec minikube docker pull orson88/recsys:backend
docker exec minikube docker pull orson88/recsys:frontend
kubectl apply -f /home/orson88/singlecluster/pod_configs/.
kubectl apply -f /home/orson88/singlecluster/main_services/back/.
kubectl apply -f /home/orson88/singlecluster/main_services/front/.

echo "waiting for pods for 10sec" 
sleep 10
kubectl port-forward frontend 5454:5454&&kubectl port-forward backend 8080:8080

