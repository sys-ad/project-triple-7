#!/bin/bash


cd ~/project-triple-7/
source python3-virtualenv/bin/activate
git fetch && git reset origin/main --hard

docker compose down
docker compose up -d --build
