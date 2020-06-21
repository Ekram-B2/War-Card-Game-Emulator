#!/bin/bash

docker build -t python-war-backend .

WORKING_DIR=$(pwd) 
docker run -v "$WORKING_DIR:/root" -p 8080:8080 python-war-backend:latest
