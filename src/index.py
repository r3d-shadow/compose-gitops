import os
import subprocess
import shutil
import yaml
import schedule
import time
from git_helper import monitor_change as git_monitor_change
from docker_helper import docker_compose_up, docker_system_prune

deploy_path = "/deploy"
repositories_file = "/src/repositories.yaml"

def main():
    # Read repositories from YAML file
    with open(repositories_file, 'r') as file:
        data = yaml.safe_load(file)
        repositories = data.get('repositories', [])

    # Iterate over repositories
    for repo in repositories:
        repository = repo.get('repository', '')
        branch = repo.get('branch', '')
        oauth2Token = repo.get('oauth2Token', '')
        dockerComposePath = repo.get('dockerComposePath', '')

        # Clone the repository
        subprocess.run(['git', 'clone', f'https://oauth2:{oauth2Token}@{repository}', '--depth', '1', '--single-branch', '--branch', branch], cwd=deploy_path, check=True)
        repo_name = os.path.basename(repository).rstrip('.git')
        repo["dockerComposePath"] = os.path.join(deploy_path, repo_name, dockerComposePath)
        del repo["oauth2Token"]
    return repositories


def monitor_change(repositories):
    for repostory in repositories:
        os.chdir(repostory["dockerComposePath"],)
        git_monitor_change_result = git_monitor_change(repostory["branch"])
        if(git_monitor_change_result):
            docker_compose_up()
            docker_system_prune()


# Schedule the job to run every minute
main_result = main()
schedule.every(10).seconds.do(monitor_change, repositories=main_result)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)
