#!/bin/bash

sudo docker build --tag ticketagency -f Dockerfile

sudo docker run --name ticketagency -p 5432:5432 -e POSTGRES_PASSWORD=mypass -d ticketagency