#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR

git config --global --add safe.directory $SCRIPT_DIR
# Get the latest commit hash of the local branch
LOCAL_COMMIT=$(git rev-parse HEAD)

# Fetch the latest changes from the remote repository
git fetch

# Get the latest commit hash of the remote branch
REMOTE_COMMIT=$(git rev-parse origin/main)

# Compare the local and remote commit hashes
if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
  echo "$(date): Changes detected in Git repository."
  ./restart.sh
else
  echo "$(date): No changes in Git repository. Deployment skipped."
fi