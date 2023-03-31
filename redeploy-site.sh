#!/bin/bash


cd ~/project-triple-7/
git fetch && git reset origin/main --hard
docker compose down
docker compose up -d --build
