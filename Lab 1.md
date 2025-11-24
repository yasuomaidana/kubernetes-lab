## Kubernetes examples

### Lab Minikube (based on official tutorial on https://kubernetes.io)

1. Launch GitHub Codespace
2. Run `minikube start` to start cluster
3. Run `minikube dashboard --url` to view dashboard in a new terminal
   > Run this `minikube dashboard` if the dashboard doesn't open automatically or when running in a remote environment (
   like Codespaces). The command prints a `--url` link you can open in your browser to access the cluster dashboard.

4. Hover over link and "follow link"
5. Create a deployment:
   `kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080`
    > Note: The `--` separates `kubectl` options from the command executed inside the container. `agnhost` is the test
    image and `netexec` is its network helper subcommand; `--http-port=8080` tells `netexec` to serve HTTP on port
    `8080`.
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
