docker ps
docker stop aed-map
docker rm aed-map
docker image rm aed-map
docker build --tag aed-map ./
docker image ls
# Dev
# docker run -d --name aed-map -p 8080:80 aed-map 
# Prod
docker run -d --name aed-map -p 443:80 aed-map 
