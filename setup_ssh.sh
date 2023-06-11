#!/bin/sh

# apply actual ssh cervice yaml config
kubectl apply -f app/ssh.yaml

# init tunnel to create external IPs
nohup minikube tunnel &

# find external ID
kubectl get services

# now you can shh to open-ssh service: ssh admin@127.0.0.1 -p 2222

# to close the tunnel find it's PID running 'ps' command, it's CMD = 'minikube tunnel'. Then kill it by PID
