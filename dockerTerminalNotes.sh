#Gives you help on how to build docker images
docker build --help

#Shows you where the docker file is located
docker --file

#Set tags while you build a docker image
docker build --tag hello-world .
#Creates a node called hello-world in current directory
#This will search for a Dockerfile and excecute the commands
#Can also use -t to tag
docker build -t dockertutorial .
#Names the new repo dockertutorial

#You can list all the images on your machine
docker images

#Running an image with docker
docker run hello-world
#Runs hello-world image on localhost
#If it can't find the image locally it will pull from docker hub

#Cloning a git repo using docker and names the container alpine/git, labelling it as a repo
docker run --name repo alpine/git clone https://github.com/docker/getting-started.git
#Copy the repo into current directory
docker cp repo:/git/getting-started/ .

#Remove an image
docker rmi imageName
#Be sure to check ps -a to remove any containers using an image first

#Check what processes are currently running (ps is processes)
docker ps
#Can also see history of ps's, included closed ones
docker ps -a

#Start and stop an image
docker start contName
docker stop contName

#List of containers in system
docker container ls -a

#Remove a container
docker rm contName
#If name doesn't work, use second name assigned, usually two random words

#You have to set a port from local machine to virtual Env
docker run -p 8080:80 hello-world
#Sets local port 8080 to virtual env port 80

#Set a custom name to the image
docker run --name contName hello-world

#You can run servers detached, good for long running servers
docker run -d hello-world

#To see the container, open browser to localhost:8080
#It will be whatever port you set in -p setting when running

#You can see logs from a container
docker logs -f contName
#-f tells it to follow the logs, ^C to escape

#Purge environment of all processes, images, etc
docker system prune -a

#Connect to a container's bash
docker exec -it contName /bin/bash
#If you connect to db container you can run queries

#Within MYSQL, connect to the db CLI
mysql -p

#You need to create a new repo in Docker to push files to

#You have to tag your image to push to repo
docker tag hello-world username/repo

#Once you create the new repo, push your local images
docker push username/repo
#Push the image you created for the repo with that tag
docker push username/repo:tag

#You can pull from repo as well
docker pull username/repo

#Networking
#List all Docker networks
docker network ls

#Inspect a network for all information in terms of docker
docker network inspect networkname
#Make sure it's in your hosts file

#DOCKER COMPOSE
#Using compose file with image from php site
docker-compose up
#Make sure you're in dir of where compose.yml file is
#Also make sure you apt installed docker-compose

#Once the server is running, go to 127.0.0.1:8000 to check it running
#8000 is port that is set in compose.yml file
#If you see forbidden page, it's working but need to make an index.php file
