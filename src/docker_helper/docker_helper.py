import docker
client = docker.from_env()

def docker_system_prune():
    try:
        client.containers.prune()
        client.volumes.prune()
        client.networks.prune()
        print("Docker system prune successful")
    except docker.errors.APIError as e:
        print(f"Docker system prune failed with error: {e}")