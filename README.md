# Minikube Cluster Initialization

This repository shows how to launch a Minikube cluster and open localhosts on ports 3000 and 5454.

## Requirements

- Docker
- Linux
- Minikube
- Bash

## Usage

1. Clone the repository.

`git clone https://github.com/username/repository.git`


2. Navigate to the repository.

`cd repository`


3. Make the script executable.

`chmod +x cluster-init.sh`


4. Launch Minikube cluster using the script.

`./cluster-init.sh`


5. Verify that the Minikube cluster is running.

`minikube status`


6. Access the localhosts on ports 3000 and 5454.

`http://localhost:5454/`

7. Access Grafana by running 
`minikube service grafana-ext`


This will provide you with the URL to access the service. Open the URL in a web browser.

## Conclusion

You've successfully launched a Minikube cluster and accessed localhosts on ports 3000 and 5454 using the instructions provided in this README.md file.
