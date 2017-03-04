NippyKindLangur
===

Flask in Docker that has one endpoint and a CLI for running it

1. Build a container with a simple flask app
---

+ Create a resftul flask app that runs inside a container
+ Once the container is started you should be able to make a curl call (GET) from outside the container to http://localhost:8888/hello and have it return { "result": "hello world" }
+ Add a docker healthcheck to your container that curls the app internally (https://docs.docker.com/engine/reference/builder/#/healthcheck)
+ Health check interval: 5s
+ Store the container in a docker registry

**Automated build available at [the Docker Hub](https://hub.docker.com/r/sudomilk/nippykindlangur/)**


2. Build a CLI in python to interact with your container
---

Commands:

```
$ dockcli run <container name>
$ dockcli stop <container name>
```

Requirements:

+ can pip install --editable
+ name: dockcli
+ container runs deamonized via CLI
+ arity 2: run|stop, container name
+ run return success: Your app is running on address, return code 0
+ run return failure: unspecified, return code non-zero
+ stop return: stop and clean up container, return code 0

Extras:

+ functional or unit tests of CLI

***

Tools to use
---

+ CLI Framework: [Python click](http://click.pocoo.org/5/)
+ Python docker module: [docker-py](https://github.com/docker/docker-py)
+ [Docker](https://www.docker.com/)
+ [Flask](http://flask.pocoo.org/)
