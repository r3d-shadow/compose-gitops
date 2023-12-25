import subprocess
import sys
from datetime import datetime

def monitor_change(branch):
    git_dir = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()

    subprocess.run(["git", "config", "--global", "--add", "safe.directory", git_dir], check=True)

    # Get the latest commit hash of the local branch
    local_commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()

    # Fetch the latest changes from the remote repository
    subprocess.run(["git", "fetch"], check=True)

    # Get the latest commit hash of the remote branch
    remote_commit = subprocess.run(["git", "rev-parse", f"origin/{branch}"], capture_output=True, text=True, check=True).stdout.strip()
    if local_commit != remote_commit:
        print("{}: Detected some changes in Git repository.".format(datetime.now()))
        return True
    else:
        print("{}: No changes in Git repository. Deployment skipped.".format(datetime.now()))
        return False

def git_pull():
    try:
        subprocess.run(["git", "pull"], check=True)
        print("Git pull successful")
    except subprocess.CalledProcessError as e:
        print(f"Git pull failed with error: {e}")