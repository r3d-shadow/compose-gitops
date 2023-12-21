#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR

git pull

#docker run --rm -i public.ecr.aws/aws-cli/aws-cli ecr get-login-password --region REGION_NAME | docker login -u AWS --password-stdin ACCOUNT_ID.dkr.ecr.REGION_NAME.amazonaws.com

docker compose up -d --build
docker system prune -f