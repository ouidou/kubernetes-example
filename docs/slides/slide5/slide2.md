## Déploiement de pod

### Qu'est-ce qu'un pod ? 

- Pod : plus petite entité de Kubernetes. La maison du container.
- Il peut contenir plusieurs containers.
- Il a une ip interne sur le cluster
- On le déploie dans un namespace (formalité de nommage)

Nous allons voir comment nous pouvons déployer un pod au travers d'un fichier .yaml.

C'est dans ce fichier que nous définissons tout ce que nous déployons sur le cluster.