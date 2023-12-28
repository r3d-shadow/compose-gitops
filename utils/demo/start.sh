#!/bin/bash
figlet -c -f Puffy "Compose Gitops" | lolcat --duration="1" -a
# Function to print command and wait
function run_command {
    echo "----------------------------------------------------------------------"
    echo "Running command: $1"
    eval $1
    sleep 3s
    echo ""
    echo ""
    echo ""
}

echo "Login to the dockerhub"
run_command "cat ~/docker.token | docker login -u redsh4d0w --password-stdin"

echo "Repository file configuration: I am using a public repository and the main branch of the same."
run_command "cat repositories.yaml"

echo "Bring up the Docker Compose services of compose-gitops"
run_command "docker compose up -d"

echo "Watch Docker containers"
run_command "watch docker ps -a"

echo "The helloworld container is up"

echo "Doing some changes to the helloworld repository"
run_command "cd ../helloworld"
run_command "echo \"$(date)\" >> README.md"
run_command "git add README.md"
run_command "git commit -m \"testing\""
run_command "git push"

echo "Monitor Docker containers to check if the new 'helloworld' container has been deployed."
run_command "watch docker ps -a"

figlet -c -f Puffy "Thank You" | lolcat --duration="1" -a