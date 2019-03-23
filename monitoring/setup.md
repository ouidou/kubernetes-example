# Installation de Prometheus Operator

Prometheus Operator est une solution toute en un de monitoring pour un cluster Kubernetes.

## Installation avec le chart helm basique

```console
helm install --name monitoring stable/prometheus-operator
```

## Désinstallation

```console
helm delete monitoring
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

CRDs created by this chart are not removed by default and should be manually cleaned up:

```console
kubectl delete crd prometheuses.monitoring.coreos.com
kubectl delete crd prometheusrules.monitoring.coreos.com
kubectl delete crd servicemonitors.monitoring.coreos.com
kubectl delete crd alertmanagers.monitoring.coreos.com
```

## Installation avec des valeurs données

```console
helm install --name my-release stable/prometheus-operator -f values.yaml
```

## Configuration de Grafana avec un subPath dans l'url

Pour faire fonctionner Grafana sur un relative path il faut modifier la configuration du ingress ainsi que le fichier de configuration `grafana.ini` se trouvant dans le configMap de Grafana.

### Configuration du grafana.ini

Il faut ajouter la configuration du nom de domaine et du relative path dans le fichier `grafana.ini` dans le configMap de grafana

```console
kubectl edit cm monitoring1-grafana
```

> Commande pour récupérer le configMap

```yaml
apiVersion: v1
data:
  grafana.ini: |
    [server]
    domain = meetkube-ouidou.westeurope.cloudapp.azure.com
    root_url = https://meetkube-ouidou.westeurope.cloudapp.azure.com/grafana
    [analytics]
```

> Ici il va falloir ajouter les 3 lignes à partir de `server` pour ajouter la configuration du domaine ainsi que la l'URL
> Attention il faut impérativement spécifier le chemin complet sur le domaine pour que grafana fonctionne.

### Configuration de l'ingress

```yaml
- path: /grafana/
    backend:
      serviceName: monitoring1-grafana
      servicePort: 3000
```

> La configuration de l'ingress doit prendre le path de l'url qui va être utilisé pour notre service ainsi que le port et le nom du service que l'on doit exposer

### Configuration du chart Helm

Nous avons ajouté ces infomrations dans le chart de prometheus operator : 

```yaml
hosts:
  - meetkube-ouidou.westeurope.cloudapp.azure.com
routePrefix: /grafana/
```