# Deploy Machine Learning Pipeline on the Azure cloud using Docker Container
## Bank_Note_Authentication ML-Model-Using-Flask
Bank Note Authentication using Machine Learning from development to deployment

This is a Project to elaborate how Machine Learn Models are deployed on production using Flask API and deploy on Azure 

## Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

Project Structure
This project has four major parts :

classifier.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
flask_api.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

# 9-steps to deploy a ML pipeline in docker container:
👉 Step 1 — Download Docker 

👉 Step 2 — Create a Dockerfile
The first step of creating a Docker image is to create a Dockerfile. A Dockerfile is just a file with a set of instructions. 

👉 Step 3— Create Azure Container Registry
* Login on https://portal.azure.com.
* Click on Create a Resource.
* Search for Container Registry and click on Create.
* Select Subscription, Resource group and Registry name (in our case: tariq.azurecr.io is our registry name)

👉 Step 4— Build Docker Image
Once a registry is created in Azure portal, the first step is to build a docker image using command line. Navigate to the project folder and execute the following code.
docker build -t tariq.azurecr.io/bank-note:latest . 
* tariq.azurecr.io is the name of the registry that you get when you create a resource on Azure portal.
* bank-note is the name of the image and latest is the tag. This can be anything you want.

👉 Step 5— Run container from docker image
Now that the image is created we will run a container locally and test the application before we push it to Azure Container Registry. To run the container locally execute the following code:

docker run -d -p 5000:5000 tariq.azurecr.io/bank-note

Once this command is successfully executed it will return an ID of the container created.

👉 Step 6 — Test container on your local machine
First type localhost:5000 on your broswer You can see the app in action by going to localhost:5000 in your internet browser. It should open up a web app.

Make sure that once you are done with this, you stop the app using following command, otherwise, it will continue to utilize resources on your computer.
This command show your container list from the list copy container id 

docker container ls 
docker container stop <container_id>

👉 Step 7— Authenticate Azure Credentials
One final step before you can upload the container onto ACR is to authenticate azure credentials on your local machine. Execute the following code in the command line to do that:

docker login tariq.azurecr.io

You will be prompted for a Username and password. The username is the name of your registry (in this example username is “tariq”). You can find your password under the Access keys of the Azure Container Registry resource you created.

👉 Step 8— Push Container onto Azure Container Registry
Now that you have authenticated to ACR, you can push the container you have created to ACR by executing the following code:

docker push tariq.azurecr.io/bank-note:latest

Depending on the size of the container, the push command may take some time to transfer the container to the cloud.

👉 Step 9— Create a Azure Web App and see your model in action
* To create a web app on Azure, follow these steps:
* Login on https://portal.azure.com.
* Click on Create a Resource.
* Search for Web App and click on Create.
* Link your ACR image that you pushed in (step 9 above) to your app.

BOOM!! The app will be up and running on Azure Web Services.
