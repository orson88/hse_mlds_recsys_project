#!/bin/bash
kubectl delete --all all
minikube stop
minikube start
docker exec minikube docker pull orson88/recsys:backend
docker exec minikube docker pull orson88/recsys:frontend
kubectl apply -f /home/orson88/singlecluster/pod_configs/.
kubectl apply -f /home/orson88/singlecluster/main_services/back/.
kubectl apply -f /home/orson88/singlecluster/main_services/front/.
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
helm install grafana grafana/grafana
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


echo "waiting for pods for 10sec" 
sleep 10
kubectl port-forward frontend 5454:5454&&kubectl port-forward backend 8080:8080

