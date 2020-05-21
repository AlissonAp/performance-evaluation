#!/bin/bash

docker rm -f flaskapi

docker build -t flaskapi .

docker run -d -p 5000:5000 --name flaskapi flaskapi