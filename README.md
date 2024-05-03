# Getting started with Milvus cluster and K8s

## Introduction
[Milvus](https://github.com/milvus-io/milvus) is a distributed vector database that aims to store, index and manage massive embedding vectors. Its ability to efficiently index and search through trillions of vectors makes Milvus a go-to choice for AI and machine learning workloads.

Kubernetes (K8s), on the other hand, excels in managing and scaling containerized applications. It provides features like auto-scaling, self-healing, and load balancing, which are crucial for maintaining high availability and performance in production environments.

## Prerequisites
* Docker - Ensure Docker is installed on your system.
* Kubernetes - Have a Kubernetes cluster ready. You can use minikube for local development or a cloud provider's Kubernetes service for production environments. For this tutorial, I will use [k3d](https://k3d.io/v5.6.3/)
* Helm - Install Helm, a package manager for Kubernetes, to help you manage Kubernetes applications, you can check our documentation to see how to do that https://milvus.io/docs/install_cluster-helm.md
* Kubectl - Install kubectl, a command-line tool for interacting with Kubernetes clusters, to deploy applications, inspect and manage cluster resources, and view logs.

### Nice to have
* [K9s](https://k9scli.io/) - Terminal based UI to interact with your Kubernetes clusters. It makes it easier to navigate, observe and manage your deployed applications in the wild.

## Setting up K8s
* Create your cluster with: `k3d cluster start`
* Check the status of your K8s cluster: `kubectl cluster-info` 


## Deploying Milvus on K8s
1. Get the Helm values: `helm show values milvus/milvus > milvus_helm.yaml`
1. Install Milvus on your cluster: `helm upgrade --install --values milvus_helm.yaml milvus milvus/milvus --namespace milvus --create-namespace`
1. Port forward the Milvus proxy to your laptop: `kubectl port-forward svc/my-milvus 19530:19530`

## Insert Data in your Milvus Cluster
Check out the [Jupyter Notebook](getting_started.ipynb) showing you how to insert data in your cluster.

--- 
Feel free to check out [Milvus](https://github.com/milvus-io/milvus), and share your experiences with the community by joining our [Discord](https://discord.gg/FG6hMJStWu).

