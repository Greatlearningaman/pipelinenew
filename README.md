# Flask Calculator App

**Technologies:** Flask, Flask-Restx, Python, Docker

## Description

Simple web application with various endpoints for different arithmetic operations to demonstrate Continuous Integeration/Continuous Delivery using Webhooks

## Run

```bash
pip3 install -r requirements
python3 app.py -m flask run
```

## Dockerization

### Running the containerized version of the app:
```bash
docker-compose up
```

We can access the app by typing `localhost:5000` in the browser.

### To stop the container and remove the created containers and images:
```bash
docker-compose down
```

### Credit

Created by interns at Citicorp Services India Private Limited, Chennai CSC, to demonstrate knowlege of Git, Docker, Jenkins and OpenShift.
