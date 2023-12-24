#!/bin/bash

# Check if the branch name argument is provided
if [ $# -eq 0 ]; then
  echo "Error: Branch name not provided. Usage: $0 <branch_name>"
  exit 1
fi

BRANCH_NAME=$1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

git config --global --add safe.directory "$SCRIPT_DIR"

# Get the latest commit hash of the local branch
LOCAL_COMMIT=$(git rev-parse HEAD)

# Fetch the latest changes from the remote repository
git fetch

# Get the latest commit hash of the remote branch
REMOTE_COMMIT=$(git rev-parse origin/$BRANCH_NAME)

# Compare the local and remote commit hashes
if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
  echo "$(date): Changes detected in Git repository."
  git pull
  docker compose up -d --build
  docker system prune -f
else
  echo "$(date): No changes in Git repository. Deployment skipped."
fi
