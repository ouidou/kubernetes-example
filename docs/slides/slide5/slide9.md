## Notre déploiement

Qu'est-ce que c'est ? 
Vous connaissez docker-compose ?
On est pas trop loin.

```yaml
apiVersion: extensions/v1beta1
  kind: Deployment
  metadata:
    labels:
      app: myapp
    name: myapp
  spec:
    replicas: 1
    template:
      metadata:
        labels:
          app: myapp
```