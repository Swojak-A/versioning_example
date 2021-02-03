#!/usr/bin/env bash
PROJECT_DIR='/home/swa/Py_Projects/versioning_example'
REPOSITORY=$PROJECT_DIR/.git
ENV_FILE=$PROJECT_DIR/.env
VERSION=$(git --git-dir=$REPOSITORY describe --tags `git --git-dir=$REPOSITORY rev-list --tags --max-count=1`)

grep -q '^VERSION' $ENV_FILE && \
        sed -i "s/^VERSION.*/VERSION=${VERSION}/" $ENV_FILE || \
        echo "VERSION=$VERSION" >> $ENV_FILE

cd $PROJECT_DIR/ || exit

git fetch --all
git checkout --force origin/master
docker-compose -f docker-compose.yml build --force-rm --no-cache web

docker-compose -f docker-compose.yml up --no-deps -d db
echo "Deployed db"
docker-compose -f docker-compose.yml up --no-deps -d web
echo "Deployed web"
docker image prune -f
echo "Cleaned old images"
