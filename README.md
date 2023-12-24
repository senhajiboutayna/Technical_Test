## Overview
This microservice interacts with the OpenAI ChatGPT API to provide answers to user-submitted questions. The answers are stored in a local CSV file for future reference.

## Directory Structure

•	app.py # Main application file
•	requirements.txt # Dependencies 
•	tests_app.py/ # structure the tests using the pytest framework
•	README.md # Project documentation
•	Dockerfile.dockerfile # script used to create a Docker image.

## Docker Container Issues

During the development of this project, several challenges were encountered in the process of building a Docker container. Some of these issues have been addressed.
1. Docker Container Build Failure
- **Issue**: Encounter errors during Docker container build
2. Docker Container Run Failure
- **Issue**: Unable to run the Docker container.
3. Docker Hub Authentication
- **Issue**: Encounter authentication errors when pushing to Docker Hub.
4. Docker Container Access Denied
- **Issue**: Receive an "access denied" error for the Docker container.
5. Docker Container Network Issues
- **Issue**: Docker container cannot connect to the network.
6. ImportError: cannot import name 'url_quote'
- **Issue**: Encounter an ImportError during the Docker container build related to 'url_quote'.

