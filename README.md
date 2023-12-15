# FastAPI


## How to run docker container

docker build --tag aed-location-map ./

docker run -d --name aed-location-map -e name='schnell' -p 80:8080 aed-location-map
