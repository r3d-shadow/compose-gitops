import subprocess

def docker_compose_up(compose_file="docker-compose.yml"):
    try:
        subprocess.run(["docker-compose", "-f", compose_file, "up", "-d", "--build"], check=True)
        print(f"Docker Compose up successful using {compose_file}")
    except subprocess.CalledProcessError as e:
        print(f"Docker Compose up failed with error: {e}")