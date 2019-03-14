## Le service

- Il expose un/des pod(s) sur le réseau du cluster
- Il peut permettre de faire du load balancing entre les pods

```yaml
apiVersion: v1
  kind: Service
  metadata:
    labels:
      app: myapp
    name: myapp
  spec:
    ports:
    - name: "8090"
      port: 8090
      targetPort: 8090
    selector:
      app: myapp
```