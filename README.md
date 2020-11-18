# Python-Microservice
An extremely simple python microservice using docker containers.

Each service will have its own Dockerfile, and they will
communicate between them.

Will contain two services:
1. Service1: A simple python script will take a JSON file, convert to XML and encrypt the XML file
2. Service2: A simple python script will use the encrpyted file and decrypt it

Shell script will be used for automating the docker-containers Deployment

How to execute?
1. Through docker-compose:
```
docker-compose up
```
2. Through shell script:
```
./runner.sh
```
