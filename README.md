# flask_kubernetes

eval $(minikube -p minikube docker-env) 

docker build -t="flask_app_to_test_kube" . 

kubectl apply -f flask-services.yml -f flask-deployment.yml 

minikube service flaskservice
|-----------|--------------|-------------|---------------------------|
| NAMESPACE |     NAME     | TARGET PORT |            URL            |
|-----------|--------------|-------------|---------------------------|
| default   | flaskservice |        6000 | http://192.168.49.2:31205 |
|-----------|--------------|-------------|---------------------------|
🎉  Opening service default/flaskservice in default browser...
 6:56PM @Bharath ~ Gtk-Message: 18:56:36.217: Failed to load module "canberra-gtk-module"
Gtk-Message: 18:56:36.224: Failed to load module "canberra-gtk-module"




curl -i http://192.168.49.2:31205/display
