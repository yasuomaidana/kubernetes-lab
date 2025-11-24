## Task 2: Deploy with Kubernetes FastAPI app

1. Push container to DockerHub (Optional): i.e.
   `docker build -t <hub-user>/<repo-name>[:<tag>]` and `docker push <hub-user>/<repo-name>:<tag>`
   Example of a pushed FastAPI container here:  https://hub.docker.com/repository/docker/noahgift/fastapi-kube
   > If you had already built your container, you can tag using `docker tag <image-id> <hub-user>/<repo-name>:<tag>` and
   then push using `docker push <hub-user>/<repo-name>:<tag>`
2. `minikube start`
3. `minikube dashboard --url`
4. Hover over link and "follow link"
5. Create a deployment: `kubectl create deployment hello-fastapi --image=yasuomaidana/kubernetes-lab:v1.0`
6. View deployment: `kubectl get deployments`
7. Create service and expose it: `kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080`
8. View services:  `kubectl get service hello-fastapi`
9. `minikube service hello-fastapi --url`
10. Curl web service: i.e. `curl http://192.168.49.2:31224`
11. Cleanup
12. Cleanup

```bash
kubectl delete service hello-fastapi
kubectl delete deployment hello-fastapi
minikube stop
````

## Notes below

### Debugging Tips

Accessing a Minikube service running inside a Dev Container requires two stages of forwarding:

Stage 1: Forward traffic from the Minikube cluster to the Dev Container's localhost.

Stage 2: Forward traffic from the Dev Container's localhost to your actual machine (Host) using VS Code.

Here are the three best methods to achieve this, ranked from easiest to most robust.

1. **Using `minikube service` Command** (Easiest):

   The `minikube service` command automatically handles the necessary port forwarding for you.

   Example:

   ```bash
   minikube service hello-fastapi --url
   ```

   This command will provide you with a URL that you can use to access the service directly from your host machine.
2. `kubectl port-forward` **(Most Robust)**
   This is often more reliable than minikube service because it forwards a specific port directly from the pod/service
   to your Dev Container, bypassing Minikube's internal networking quirks.
    1. Find your Service or Pod name:
       ```shell
        kubectl get services
        ```
    2. Forward the port: Run this in your terminal. Replace service/my-service with your actual service name.
       ```shell
       # Syntax: kubectl port-forward <resource> <local-port>:<container-port>
       kubectl port-forward service/my-service 8080:8080 --address 0.0.0.0
       ```
        - `--address 0.0.0.0` ensures the Dev Container listens on all interfaces, which helps VS Code detect the port
          easier.
        - `8080:8080` maps port `8080` on the container to port `8080` on the service. Change the first number if you
          want a different local port.
    3. Access in Browser:
        - VS Code's Ports view will show port 8080.
        - Click the Globe icon or open http://localhost:8080 in your local browser.
3. `minikube tunnel` (For LoadBalancers)
   This method is useful if you're using LoadBalancer services in Minikube.
    1. Start the tunnel:
        ```shell
        minikube tunnel
        ```
       This command requires admin privileges because it creates network routes on your host machine.
    2. Access the Service:
        - Use `kubectl get services` to find the external IP assigned to your LoadBalancer service.
        - Access the service using that IP and the specified port.
        ```bash
       sudo minikube tunnel
       ```
    3. Watch the service : 
       ```shell
       kubectl get svc -w
       ```
       Wait until the `EXTERNAL-IP` changes from `<pending>` to an IP address (usually 10.xx.xx.xx or similar).
    4. Forward the Traffic: Because the `EXTERNAL-IP` is still inside the Dev Container, you still need to bridge it to
       your host. It's usually easier to combine this with Method 2 (Port Forwarding) targeting that specific service port.

Troubleshooting

- **"Connection Refused"**: Ensure you are using the port listed in the VS Code Ports view, effectively the "Forwarded
  Port," not necessarily the port inside the container.

- **Persisting Ports**: If you want a port (e.g., `8080`) to be always available, add it to your
  `.devcontainer/devcontainer.json` file:

```
"forwardPorts": [8080],
"portsAttributes": {
"8080": {
"label": "Minikube Service",
"onAutoForward": "notify"
}
}
```