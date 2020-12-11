#!/bin/bash

sudo podman build --tag ticketagency -f Dockerfile

sudo podman run --name ticketagency --systemd=true --ip 10.88.25.25 -e POSTGRES_PASSWORD=mypass -d ticketagency