# Minikube Cluster Initialization

This repository shows how to launch a Minikube cluster and open localhosts on ports 3000 and 5454.

## Requirements

- Docker
- Linux
- Minikube
- Bash

## Usage

1. Clone the repository and switch to arspoz branch.

`git clone https://github.com/username/repository.git`


2. Navigate to the repository.

`cd repository`


3. Launch Minikube cluster using the script.

`sh cluster-init.sh`


4. Verify that the Minikube cluster is running.

`minikube status`


5. Access the localhosts on ports 3000 and 5454.

`http://localhost:5454/`

6. Access Grafana by running 
`minikube service grafana-ext`


This will provide you with the URL to access the service. Open the URL in a web browser.

## Conclusion

You've successfully launched a Minikube cluster and accessed localhosts on ports 3000 and 5454 using the instructions provided in this README.md file.
