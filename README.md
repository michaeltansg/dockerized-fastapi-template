# dockerized-fastapi-template
A template for FastAPI with Docker and Dev Containers.

## Getting started
1. Create a `.env` file.
2. Rename the service `app` and modify the container_name value (`fastapi-server`) in docker-compose.yml file as appropriate.
3. Start the container using: `docker compose up -d`
4. Check the service is running. The following are expected behaviour:

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

To create an image for distribution, modify the `Dockerfile` (if required) and then execute: `docker build -t app_name:latest .`

---

To install python packages on host:
```bash
python -m venv venv;. venv/bin/activate; pip install -U pip
pip install -r requirements.txt
```

If more packages are added to requirements.txt, execute the following: `docker compose up --build -d` to rebuild the docker image and start a new container.
