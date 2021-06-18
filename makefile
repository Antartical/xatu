#!make
.DEFAULT_GOAL=start

local.build:
	@docker-compose build

local.start:
	@docker-compose up -d

local.down:
	@docker-compose down

local.test:
	@docker exec xatu pytest --cov=xatu

ci.test:
	@docker-compose run -v $(PWD):/app xatu coverage run --source=xatu -m pytest
	@mv .coverage .coverage-docker
	@coverage combine -a .coverage-docker
	@coverage report

logs:
	@docker logs -f $(shell docker-compose ps -q xatu)
 
sh:
	@docker exec -it xatu /bin/bash

ci.docker.login:
	@echo $(GITHUB_TOKEN) | docker login ghcr.io -u $(GITHUB_USER) --password-stdin

docker_tag_and_push: ci.docker.login
	@export TAG=$(date +%d%m%Y-%H%M%S)
	@docker build -f build/docker/dockerfile.prod -t $(REGISTRY):latest -t $(REGISTRY):$(TAG) .
	@docker push $(REGISTRY):$(TAG)
	@docker push $(REGISTRY):latest

dependencies.upgrade:
	@docker exec -it xatu poetry update

start: local.start

stop: local.down

renew: local.down local.build local.start

ci_check_tests:ci.docker.login local.start ci.test

.PHONY:  start stop renew sh logs docker_tag_and_push
