## Publier un service

Pour publier un service on peut utiliser quatre outils différents :

- ClusterIP : c'est une ip interne joignable uniquement dans le cluster
- NodePort : on expose sur l'IP du **node** sur un port static joignable de l'extérieur
- LoadBalancer : on créé un LB avec ce que propose le cloud provider
- ExternalName : on expose le service sur un dns directement. *nécessite kube-dns*