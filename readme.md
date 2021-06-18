[![Build Status](https://travis-ci.com/Antartical/xatu.svg?branch=main)](https://travis-ci.com/Antartical/xatu)
[![Coverage Status](https://coveralls.io/repos/github/Antartical/xatu/badge.svg?branch=master)](https://coveralls.io/github/Antartical/xatu?branch=master)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<p align="center">
  <img width="260" height="240" src="https://i.imgur.com/xqlXzKf.png">
</p>

## Xatu in a nutshell

Xatu is the only one who can actually forecast what your users wants. This service allow us
to perform recommendations for the users based on their preferences by using a graph based database.

## Local development

Xatu is easy to develop in a local environment by using docker. just type in your terminal `make`
and everything you need will make up by itselt. Please copy the content of `build/env/.env.sample` to
your own _.env_ in `build/env/.env`. You can do this by executting:

```cmd
cp ./build/env/.env.sample ./build/env/.env
```

Moreover you can perform the following operations:

- **make**: setting up the containers
- **make sh**: attach a console inside xatu.
- **make logs**: shows xatu logs
- **make local.build**: recompiles xatu image
- **make dependencies.upgrade**: upgrade all dependencies
  
## cli

Xatu has a powrful cli which can help us to perform operations directly in the system. You can get more information
about the available commands by executting
```cmd
python manage.py --help
```

## Configure pre-commit (Python3 required)

pre-commit is a useful tool which checks your files before any commit push preventings fails in early steps.

Install pre-commit is easy:

```
pip install pre-commit
python3 -m pre_commit install
```


## How to setup Xatu as a dependency in your own docker-compose

Just include the following code in your `docker-compose.yml`

```docker
arango:
  image: arangodb/arangodb
  container_name: xatu.arango
  restart: always
  environment:
    - ARANGO_ROOT_PASSWORD=root
  ports:
    - "8529:8529"
  volumes:
    - xatu.rayquaza:/var/lib/arangodb3

xatu:
  image: ghcr.io/antartical/gandalf
  container_name: xatu
  ports:
    - "9700:9700"
  environment:
  - ENVIRONMENT=docker
  - ARANGO_HOST=arango
  - ARANGO_PORT=8529
  - ARANGO_DB_NAME=_system
  - ARANGO_PASSWORD=root

volumes:
  xatu.rayquaza:
  data01:
    driver: local

```
