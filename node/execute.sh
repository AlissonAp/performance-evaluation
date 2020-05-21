#!/bin/bash

docker rm -f nodeapi

docker build -t nodeapi .

docker run -d -p 3000:3000 --name nodeapi nodeapi