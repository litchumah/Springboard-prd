#!/bin/bash


docker run -p 8000:8000 -d -it --rm instructure/dynamo-local-admin

docker pull python
docker build -t springboard .
docker run -p 9000:9000 -d -it --rm --name springboard springboard