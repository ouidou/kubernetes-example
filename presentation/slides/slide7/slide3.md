#### Créeons notre HPA

```console
kubectl autoscale deployment myapp --cpu-percent=10 --min=1 --max=15
```

Ici on spécifie : 

- Le déploiement concerné par l'horizontal pod autoscaler
- La limite de ressource pour le scaling
- Le nombre minimal de réplicas
- Le nombre maximal de réplicas