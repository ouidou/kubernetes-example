#!/bin/bash

# Ce script permet de supprimer les éléments que le helm chart ne supprime pas à la commande helm delete release

helm delete monitoring1
helm delete --purge monitoring1
kubectl delete crd prometheuses.monitoring.coreos.com
kubectl delete crd prometheusrules.monitoring.coreos.com
kubectl delete crd servicemonitors.monitoring.coreos.com
kubectl delete crd alertmanagers.monitoring.coreos.com
kubectl delete deployment myapp
kubectl delete service myapp
kubectl delete hpa myapp
