# Restaurant_demo

Name= Moustafa Youssef
LinkedIn = https://www.linkedin.com/in/moustafa-youssef-63398a116/
Email: moustafayoussef759@gmail.com



GitHub Link: https://github.com/Moustafa-youssef-linux/Restaurant_demo

##

**First**

There are two branches main and test.You can consider TEST branch for getting the last stable version.

############################################################################################################################
###################################### Application Info ####################################################################

Application is written in python flask and backed by mysql database with basic html.
The application Idea is a very simple food ordering app in which there are two dashboards one for admin so that he/she can add a restaurant and customer dashboard in which they can put orders with simple signup/signin forms

The app has been developed by me as i have some experience with developing backend apps


You can start logging in admin user using the following credentials
username: admin
password: admin@123



the available APIs:

@app.route("/")

@app.route('/login', methods=['GET', 'POST'])

@app.route('/logout', methods=['GET'])

@app.route('/registration', methods=['GET', 'POST'])

@app.route('/restaurants', methods=['GET','POST'])

@app.route('/admin_console', methods=['GET','POST'])

@app.route('/rest/create', methods=['GET', 'POST'])

@app.route('/rest/delete', methods=['GET', 'POST'])

@app.route('/rest/update', methods=['GET','POST'])

@app.route('/order', methods=['GET','POST'])

@app.route('/healthz', methods=['GET'])

@app.route('/health_db', methods=['GET'])


Note: 
In the database,I created the management table which contains a simple 
message retrieved by /health_db endpoint. In this way i can test the connection between the APP and DB.
it's added as a liveness probe inside K8s for testing connection periodically.

I also developed simple api endpoint /healthz to test app readiness.

The app is containerized.And i have two dockerfiles,Container images and pods.one for Database and other for backend app.
app container is running in port 5000 and mysql database container i running in port 3306.

both will be deployed in the same K8s namespace and the app will be the one which exposed to outside world. 

The GitOps approach will be only applied for backend application.

You can find the database container dockerfile in ./database/Dockerfile with sql script for seeding the database.

###########################################################################################################################
**Second**
###################################################### GitOps #############################################################
I've used argocd as required by the task with Helm.The ArgoCd detects the chart of the app in this path ./infrastructure/restartaurant-app and use manifests.

there's a secret resource which is created for storing db username & password
There's ConfigMap for storing database url and database name
There's a serviceaccount created for ABI-backend app pod with role and rolebinding 

Note(1):
the ingress resource is deployed and tested with nginx ingress controller of community version

Note(2):
I've used GCP artifact registry to store the images after building them.It's better so that for testing the app the K8s will pull it directly from there.

**Third**
########################################### GCP #####################################################################

1- I have built GKE as VPC-native cluster as it's more secure with two endpoint for control plan one public and other private.

2- using Cloud NAT to let compute node be able to pull container images from internet.

3- configuring workload identity federation including federation pool and serviceaccount iam policies and allow policies to let github authenticate and use resources.

4- Deploying Nginx ingress controller of community version to expose service to outside world.

5- The Ingress controller has provisioned GCP Loadbalancer which in turn will be used to forward traffic to internal GKE pods

6- Deploying Prometheus and grafana in monitoring namespace and expose granfa as ingress object http://grafana.example.com

7- Deploying Argocd in argocd namespace and exposed as ingress object http://argocd.example.com

8- Deploying Vault in vault namespace,configuring vault template,annotations so that the vault-agent can inject secrets(database username and password) into app pod.


# for anything not clear or not mentioned in ReadMe,I will be grateful to hear back from you

Email: moustafayoussef759@gmail.com
LinkedIn: https://www.linkedin.com/in/moustafa-youssef-63398a116/




