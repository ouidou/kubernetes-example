### Et pour finir

```yaml
image: docker.ouidou.fr/meetkube/myapp:latest
  name: myapp
ports:
- containerPort: 8090
resources:
requests:
  memory: "64Mi"
  cpu: "100m"
limits:
  memory: "128Mi"
  cpu: "200m"
imagePullSecrets:
  - name: regcred
restartPolicy: Always
```
$term