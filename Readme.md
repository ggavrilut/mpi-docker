# Steps
* Uncomment selected Dockerfile

# For python script
* Build docker image : docker build . -t py
* Run docker image in order to create container : docker run py

# For python HTTP Server

## Without docker-compose
* docker build . -t py
* docker run py -p 8080:8080
## With docker-compose
* create docker-compose.yml
* docker-compose up -d
