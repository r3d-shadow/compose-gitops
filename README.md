
# Compose GitOps

Compose GitOps is a tool designed to automate the deployment and synchronization of Docker Compose-based applications from multiple Git repositories. It leverages Docker Compose for managing multi-container Docker applications and Git for version control. This tool is especially useful for orchestrating deployments in a GitOps workflow.

## Prerequisites

Before using Compose GitOps, ensure that you have the following prerequisites installed:
-   Docker

## Installation &  Configuration

To quickly set up Compose GitOps, follow these steps:

1.  **Download Docker Compose Configuration:**
    
    Fetch the Docker Compose configuration directly from the GitHub repository using `curl`:
    
    bashCopy code
    
    `curl -o docker-compose.yml https://raw.githubusercontent.com/redsh4d0w/compose-gitops/main/docker-compose.yml` 
    
    This command retrieves the latest `docker-compose.yml` file from the repository.
    
2.  **Adjust Configuration Files:**
    
    -   Modify the `docker-compose.yml` file:
        
        -   Adjust the persistent storage folder by updating the volume mapping.
        -   Ensure the `repositories.yaml` file is mounted appropriately.
    -   Edit the `repositories.yaml` file:
        
        -   Include details of the Git repositories you wish to manage.
        
        1.  -   Example `repositories.yaml`:
        
        yamlCopy code
        
        `repositories:
          - repository: "github.com/redsh4d0w/helloworld.git"
            branch: "dev"
            oauth2Token: "YOUR_GITHUB_TOKEN"
            dockerComposePath: "utils/deploy"` 
        
2.  **Run Docker Compose:**
    
    Start Compose GitOps using Docker Compose:
    
    bashCopy code
    
    `docker-compose up -d` 
    
    This command launches the Compose GitOps service in the background, configured based on your adjusted `docker-compose.yml` and `repositories.yaml` files.

## Contributing

Feel free to contribute to the development of Compose GitOps. Fork the repository, make your changes, and submit a pull request.