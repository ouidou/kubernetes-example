## Ajout de grafana sur notre ingress

Nous souhaitons exposer notre Grafana sur internet en SSL.

On ajoute simplement cette configuration à notre ingress :

```yaml
rules:
  - host: meetkube-ouidou.westeurope.cloudapp.azure.com
    http:
      paths:
      - path: /grafana/
        backend:
          serviceName: monitoring1-grafana
          servicePort: 3000
```