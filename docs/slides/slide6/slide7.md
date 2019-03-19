# En pratique

```console
kubectl edit cm monitoring1-grafana
```

Et on ajoute notre configuration :

```yaml
[server]
domain = meetkube-ouidou.westeurope.cloudapp.azure.com
root_url = https://meetkube-ouidou.westeurope.cloudapp.azure.com/grafana
```