# NippyKindLangur
Flask in Docker that has one endpoint

## Build a container with a simple flask app

+ Create a resftul flask app that run inside a container
+ Once the container is started you should be able to make a curl call (GET) from outside the container to http://localhost:8888/hello and have it return { "result": "hello world" }
+ Add a docker healthcheck to your container that curls the app internally (https://docs.docker.com/engine/reference/builder/#/healthcheck)
+ Health check Interval: 5s
+ Store the container in a docker registry
