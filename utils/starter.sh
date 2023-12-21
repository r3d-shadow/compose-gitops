#!/bin/bash
cd /deploy

json_file="/utils/repositories.json"
repositories=$(jq -c '.repositories[]' "$json_file")

# Iterate over repositories
for repo in $repositories; do
    repository=$(echo "${repo}" | jq -r '.repository')
    branch=$(echo "${repo}" | jq -r '.branch')
    oauth2Token=$(echo "${repo}" | jq -r '.oauth2Token')
    git clone https://oauth2:$oauth2Token@$repository --depth 1 --single-branch --branch $branch
done

crond -f -d 8