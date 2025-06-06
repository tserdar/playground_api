#!/bin/bash
set -e

echo "Building Docker image..."
docker build . -t playground_app
cd ..
cd traefik

echo "Switching to Traefik directory..."
docker compose stop api
docker compose rm -f api
docker compose up -d

echo "Removing dangling containers and images..."
docker container prune -f
docker image prune -f

echo "Done."
