import boto3
import docker
import os
import subprocess
import base64

region_name = os.environ.get('AWS_REGION')
account_id = os.environ.get('AWS_ACCOUNT_ID')
client = boto3.client('ecr', region_name=region_name)
docker_cli = docker.from_env()

def ecr_image_pull(images=[]):
    for image in images:
        docker_cli.images.pull(image)

def ecr_image_login_and_pull(images=[]):
    try:
        response = client.get_authorization_token(
            registryIds=[
                account_id,
            ]
        )
        token = response["authorizationData"][0]["authorizationToken"]
        endpoint = response["authorizationData"][0]["proxyEndpoint"]

        username, password = base64.b64decode(response['authorizationData'][0]['authorizationToken']).decode().split(':')
        docker_cli.login(username=username, password=password, registry=endpoint)
        ecr_image_pull(images)
        print(f"Docker Image pull successful")
    except Exception as e:
        print(f"Docker Image pull failed with error: {e}")