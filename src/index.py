import os
import subprocess
import shutil
import yaml
import schedule
import time
from git_helper import monitor_change as git_monitor_change, git_pull
from docker_helper import docker_compose_up, docker_system_prune
from hooks_helper import execute_inline_script

sync_timeouts = int(os.getenv('SYNC_TIMEOUT', 5))
deploy_path = "/deploy"
repositories_file = "/src/repositories.yaml"

def main():
    # Read repositories from YAML file
    with open(repositories_file, 'r') as file:
        data = yaml.safe_load(file)
        repositories = data.get('repositories', [])

    # Iterate over repositories
    for repo in repositories:
        name = repo.get('name', '')
        source = repo.get('source', {})
        branch = source.get('branch', '')
        repo_url = source.get('repoURL', '')
        compose_path = source.get('composePath', {})
        authentication = source.get('authentication', {})
        oauth2_token = authentication.get('token', '')

        repo_name = os.path.basename(repo_url).rstrip('.git')
        repo_path = os.path.join(deploy_path, repo_name)
        repo["path"] = repo_path

        pre_deploy_script = repo.get('hooks', {}).get('preDeploy', None)
        post_deploy_script = repo.get('hooks', {}).get('postDeploy', None)

        ## ----------- Deployment: START ----------- 
        # Check if the repository directory already exists
        if os.path.exists(repo_path):
            os.chdir(repo["path"])
            # If the directory exists, set the remote URL
            subprocess.run(['git', 'remote', 'set-url', 'origin', f'https://oauth2:{oauth2_token}@{repo_url}'], cwd=repo_path, check=True)
            subprocess.run(['git', 'checkout', branch], cwd=repo_path, check=True)
        else:
            # Clone the repository
            subprocess.run(['git', 'clone', f'https://oauth2:{oauth2_token}@{repo_url}', '--depth', '1', '--single-branch', '--branch', branch], cwd=deploy_path, check=True)

        del repo["source"]["authentication"]
        os.chdir(repo["path"])

        execute_inline_script(pre_deploy_script)
        docker_compose_up(compose_path)
        docker_system_prune()
        execute_inline_script(post_deploy_script)
        ## ----------- Deployment: END ----------- 
    return repositories


def monitor_change(repositories):
    for repo in repositories:
        source = repo.get('source', {})
        branch = source.get('branch', '')
        compose_path = source.get('composePath', {})

        os.chdir(repo["path"])
        git_monitor_change_result = git_monitor_change(branch)
        if(git_monitor_change_result):
            git_pull()
            docker_compose_up(compose_path)
            docker_system_prune()


# Schedule the job to run every minute
main_result = main()
print("Main function has been completed")
schedule.every(sync_timeouts).minutes.do(monitor_change, repositories=main_result)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)
