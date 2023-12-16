# AED location map

## Tech stack
- Fastapi




## How to run docker container

docker build --tag aed-location-map ./


First build the docker image from the Dockerfile.
--tag is the build command option to add a tag name.. The tag in Docker is useful to maintain the version of the build to push the image to the DockerHub. The versioning is generally used to deploy any Docker image or get back to the older version.
./ means building the image based on the whole files in the current directory.



docker run -d --name aed-location-map-container -p 8080:80 aed-location-map

-d means running the container in background and print container ID.
1. Without -d (Foreground Mode)

    The container starts and runs in the foreground.
    The standard output (STDOUT) and standard error (STDERR) of the container are displayed in your terminal. This is useful for debugging or when you want to watch the output of your container in real time.
    Your terminal will be "attached" to the container's process, meaning you won't be able to interact with your terminal prompt until the container process stops or you manually detach from the container without stopping it (using Ctrl+P followed by Ctrl+Q in most shells).
    If you stop the container's main process (e.g., by pressing Ctrl+C), it will stop the container.

2. With -d (Detached Mode)

    The container starts and runs in the background.
    The terminal is not attached to the container's standard output or error, allowing you to continue using the terminal for other commands.
    You will receive the container ID in the output, and the container will run in the background.
    To view the logs of a container running in detached mode, you would use docker logs <container_id>.

--name
The --name flag in the docker run command is used to assign a specific name to the container you're running. Without this flag, Docker generates a random name for each container. Naming containers can be very useful for identification and management purposes.

notes
ssh -i "~/.ssh/aed-location-map-ec2.pem" ec2-user@ec2-57-181-29-44.ap-northeast-1.compute.amazonaws.com
http://localhost:8080/docs#/
