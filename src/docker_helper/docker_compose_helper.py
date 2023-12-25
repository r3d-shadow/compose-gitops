import subprocess

def docker_compose_up():
    try:
        subprocess.run(["docker-compose", "up", "-d", "--build"], check=True)
        print("Docker Compose up successful")
    except subprocess.CalledProcessError as e:
        print(f"Docker Compose up failed with error: {e}")