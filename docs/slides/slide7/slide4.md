## Chargeons notre pod

|On utilise Apache bench pour faire des requêtes sur notre appli.

```console
ab -n 10000 -c 10 "https://meetkube-ouidou.westeurope.cloudapp.azure.com/load/1"
```