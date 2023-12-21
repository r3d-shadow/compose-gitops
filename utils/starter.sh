#!/bin/bash
cd /deploy

json_file="/utils/repositories.json"
repositories=$(jq -c '.repositories[]' "$json_file")

# Iterate over repositories
for repo in $repositories; do
    repository=$(echo "${repo}" | jq -r '.repository')
    branch=$(echo "${repo}" | jq -r '.branch')
    oauth2Token=$(echo "${repo}" | jq -r '.oauth2Token')
    dockerComposePath=$(echo "${repo}" | jq -r '.dockerComposePath')
    git clone https://oauth2:$oauth2Token@$repository --depth 1 --single-branch --branch $branch
    repoName=$(basename -s .git "$repository")
    cd $repoName/$dockerComposePath
    cp /utils/gitchange.sh .
    sed -i "s/BRANCH_NAME=.*/BRANCH_NAME=$branch/" gitchange.sh
    echo $PWD/gitchange.sh >> /utils/cronjob.sh
    cp /utils/restart.sh .
    ./restart.sh
done

crond -f -d 8