## Kubernetes examples

### Lab Minikube (based on official tutorial on https://kubernetes.io)

1.  Launch GitHub Codespace
2.  Run `minikube start` to start cluster
3.  Run `minikube dashboard --url` to view dashboard in a new terminal
4.  Hover over link and "follow link"
5.  Create a deployment:  `kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080`
6. View deployment: `kubectl get deployments`
7. View pods:  `kubectl get pods`
8. Create service and expose it: `kubectl expose deployment hello-node --type=LoadBalancer --port=8080`
9. View services:  `kubectl get services`
10. Curl the url shown, for example: `curl http://192.168.49.2:31839` or change to your URL.
11. Cleanup
```bash
kubectl delete service hello-node
kubectl delete deployment hello-node
minikube stop
````
