# jenkins-monitoring
Jenkins monitoring using Prometheus stack and custom Jenkins Prometheus exporter

- build and pull all docker images: `docker-compose build`
- run the application stack: `docker-compose -p jenkins-monitoring up -d`
- Note that ports 8080, 3000, 8000, 9090 are mapped to Docker hos and must be vacant on it.
- navigate to Grafana UI at localhost:3000.
- login as `admin`, `admin`, skip password change. 
- you should see Jenkins job count metrics.
