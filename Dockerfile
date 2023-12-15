FROM python:3.10.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
# the host requires to be 0.0.0.0 instead of 127.0.0.1 because this will be deployed in the container where it needs to receive http request from the outside.
# If 127.0.0.1(localhost) was set, then it can only points to the container itself.
# Binding to 127.0.0.1 (localhost): If the server binds to 127.0.0.1, it's only reachable from the same machine on which it's running. This is a loopback address, often referred to as localhost.
# Binding to 0.0.0.0: This is a special IP address in the context of server applications. It means "all IPv4 addresses on the local machine." If a server is set up to listen on 0.0.0.0, it will accept connections on all IPv4 addresses that the host machine possesses.
CMD [ "uvicorn", "main:app", "--port", "80", "--host", "0.0.0.0" ]
