import os
import subprocess
import shutil
import yaml

deploy_path = "/deploy"
repositories_file = "/utils/repositories.yaml"

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

    # Change directory to the cloned repository
    repo_name = os.path.basename(repository).rstrip('.git')
    os.chdir(os.path.join(deploy_path, repo_name, dockerComposePath))

    # Copy gitchange.sh 
    shutil.copy('/utils/gitchange.sh', '.')

    # Append gitchange.sh path to cronjob.sh
    with open('/utils/cronjob.sh', 'a') as cronfile:
        cronfile.write(f'{os.getcwd()}/gitchange.sh {branch}\n')

    # Copy restart.sh and execute it
    shutil.copy('/utils/restart.sh', '.')
    os.system('./restart.sh')

# Run crond
os.system('crond -f -d 8')
