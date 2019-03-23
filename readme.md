# Kubernetes example

Nous avons souhaité montrer les capacités de Kubernetes au travers de la vie d'une application simple sur un cluster. Kubernetes c'est bien tout le monde vous en parle mais peu de gens vous montrent comment ça tourne. Ici nous avons fait une petite application Python que nous déployons sur un cluster Kubernetes. Nous allons mettre en place un monitoring et faire scaler cette application pour démontrer les capacités de Kubernetes.

Vous trouverez dans ce repository le support de présentation de cette demo ainsi que les fichiers de déploiement et dockerfile de notre application. 

## [Présentation](https://ouidou.github.io/kubernetes-example/docs)

## Prérequis

Pour faire fonctionner tout ce qui est ici vous allez avoir besoin de plusieurs éléments:

* Un cluster Kubernetes
* Helm [doc](https://helm.sh/docs/install/)
* Tiller [doc](https://helm.sh/docs/install/#easy-in-cluster-installation)
* Ingress
* Une registry docker pour stocker votre image (le hub docker fait l'affaire)

> Si vous ne souhaitez pas avoir vos applications en ligne vous pouvez utiliser la fonctionnalité port-forwarding de kubernetes pour accéder à vos services en local sur votre poste.

## Thèmes abordés

* Docker
* Les fichiers yaml
* Déploiement
* Service Kubernetes
* Horizontal Pod Autoscaler
* Helm
* Monitoring (w/ Prometheus & Grafana)

## Présentation

La présentation est faite en [reveal.js](https://revealjs.com/#/) et est accessible sur ce dépôt via Github Pages [ici](https://ouidou.github.io/kubernetes-example/docs).
