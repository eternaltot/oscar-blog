DOCKER_FILE_PATH = docker/dev/docker-compose.yml
PROJECT_NAME = oscar-blog

.PHONY: init start stop cleanup

init:
	echo "Build service blog..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_FILE_PATH) build
	echo "Run install dependency..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_FILE_PATH) run --rm oscar_web pip install -r requirements.txt

start:
	echo "Start container..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_FILE_PATH) up -d 

stop:
	echo "Stop container..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_FILE_PATH) stop

cleanup:
	echo "Clean container service..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_FILE_PATH) down