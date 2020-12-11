#!/bin/bash

sudo docker build --tag ticketagency -f Dockerfile

sudo docker run --name ticketagency --systemd=true --ip 10.88.25.25 -e POSTGRES_PASSWORD=mypass -d ticketagency