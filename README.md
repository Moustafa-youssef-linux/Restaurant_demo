# Restaurant_demo

Name= Moustafa Youssef
LinkedIn = https://www.linkedin.com/in/moustafa-youssef-63398a116/
Email: moustafayoussef759@gmail.com



GitHub Link: https://github.com/Moustafa-youssef-linux/Restaurant_demo



**First**

There are two branches main and test.You can consider main branch for getting the last stable version.

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

###############################################################################################

############################ K8s ###############################################################################
there is a directory called K8s under which you can find all the required resources for deploying the app on K8s

there's a secret resource which is created for storing db username & password

Note(1):
the ingress resource is deployed and tested with nginx ingress controller

Note(2):
I've used DockerHub to store the images after building them.It's better so that for testing the app the K8s will pull it directly from there.

################################################################################################################


# for anything not clear or not mentioned in ReadMe,I will be grateful to hear back from you

Email: moustafayoussef759@gmail.com
LinkedIn: https://www.linkedin.com/in/moustafa-youssef-63398a116/




