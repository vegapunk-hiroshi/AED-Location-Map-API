docker ps
docker stop aed-map
docker rm aed-map
docker build --tag aed-map ./
docker image ls
docker run -d --name aed-map -p 80:80 aed-map