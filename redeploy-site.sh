#!/bin/bash

#cd into project portfolio
cd /root/portfolio-site

#make sure to get latest github repo version
git fetch && git reset origin/main --hard

#first spin containers down to prevent out of memory issues on
#our VPS instances when building in the next step
docker compose -f docker-compose.prod.yml down

#build containers back up and -d for detach to keep it running in the background
docker compose -f docker-compose.prod.yml up -d --build