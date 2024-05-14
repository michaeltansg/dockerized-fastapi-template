# Define variables with default values
IMAGE_NAME ?= [USER_OR_ORG_NAME]/[REPOSITORY_NAME]
TAG ?= latest
PLATFORM ?= linux/amd64

# Build target
build:
	docker buildx build -t $(IMAGE_NAME):$(TAG) .

# Push target
push:
	docker buildx build --platform $(PLATFORM) -t $(IMAGE_NAME):$(TAG) --pull --no-cache --push .
