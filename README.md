# Deploy Machine Learning Pipeline on the cloud using Docker Container
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

# 10-steps to deploy a ML pipeline in docker container:
👉 Step 1 — Download Docker 

👉 Step 3 — Create a Dockerfile
The first step of creating a Docker image is to create a Dockerfile. A Dockerfile is just a file with a set of instructions. 

👉 Step 4— Create Azure Container Registry
* Login on https://portal.azure.com.
* Click on Create a Resource.
* Search for Container Registry and click on Create.
* Select Subscription, Resource group and Registry name (in our case: tariq.azurecr.io is our registry name)

👉 Step 5— Build Docker Image
Once a registry is created in Azure portal, the first step is to build a docker image using command line. Navigate to the project folder and execute the following code.
docker build -t tariq.azurecr.io/bank-note:latest . 
* tariq.azurecr.io is the name of the registry that you get when you create a resource on Azure portal.
* bank-note is the name of the image and latest is the tag. This can be anything you want.

👉 Step 6— Run container from docker image
Now that the image is created we will run a container locally and test the application before we push it to Azure Container Registry. To run the container locally execute the following code:

docker run -d -p 5000:5000 pycaret.azurecr.io/pycaret-insurance

Once this command is successfully executed it will return an ID of the container created.
