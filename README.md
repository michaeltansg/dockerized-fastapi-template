# dockerized-fastapi-template
A template for FastAPI with Docker and Dev Containers.

## Getting started
1. Create a `.env` file.
2. Modify Makefile with the appropriate image name.
3. Rename the service `app` and modify the container_name value (`fastapi-server`) in docker-compose.yml file as appropriate.
4. Start the container using: `docker compose up -d`
5. Check the service is running. The following are expected behaviour:

```bash
$ curl http://localhost
{"Hello":"World"}

$ curl http://localhost:8080/api/health/
{"now":xxxxxx}
```

### OpenAPI documentation endpoints:
http://localhost/api/docs
http://localhost/api/redoc

The project is being watched for changes and any saved modifications will cause the app to be reloaded.

To create an image for distribution, modify the `Dockerfile` (if required) and then execute: `make push`

Other examples of use of Makefile:
```
make build IMAGE_NAME=mycustomimage TAG=v1.0
make push IMAGE_NAME=mycustomimage TAG=v1.0 PLATFORM=linux/arm64
```

---

To install python packages on host:
```bash
python -m venv venv;. venv/bin/activate; pip install -U pip
pip install -r requirements.txt
```

If more packages are added to requirements.txt, execute the following: `docker compose up --build -d` to rebuild the docker image and start a new container.
