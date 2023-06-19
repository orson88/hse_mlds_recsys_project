#!/bin/bash
kubectl delete --all all
minikube stop
minikube start
kubectl apply -f /home/orson88/singlecluster/pod_configs/.
kubectl apply -f /home/orson88/singlecluster/main_services/back/.
docker exec minikube docker pull orson88/recsys:backend
