#!/bin/bash

sudo podman build --tag ticketagency -f Dockerfile

sudo podman run --name ticketagency -p 5432:5432 -e POSTGRES_PASSWORD=mypass -d ticketagency