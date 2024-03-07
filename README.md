
# Compose GitOps

Compose GitOps is a tool designed to automate the deployment and synchronization of Docker Compose-based applications from multiple Git repositories. It leverages Docker Compose for managing multi-container Docker applications and Git for version control. This tool is especially useful for orchestrating deployments in a GitOps workflow.

- **Automated Deployment:** Streamline the deployment process for Docker Compose-based applications directly from Git repositories.
- **Advanced GitOps Workflow:** Automate your workflows with predeploy and postdeploy scripts for intricate configurations.
- **Private Repository Access:** Easily manage private Git repositories for enhanced security.
- **Simplified Private Docker Images Access:** Access and manage private repositories seamlessly with an out-of-the-box solution. It allows you to handle private repositories externally.
- **Predeploy and Postdeploy Scripts:** Execute custom scripts before and after deployment for tailored configuration.
- **Flexibility:** Enjoy increased flexibility in managing private images, private GitHub repositories, and custom deployment scripts.
- **Dynamic Volume Creation:** Create volume folders dynamically within GitHub repo folders using predeploy scripts.

## Prerequisites

Before using Compose GitOps, ensure that you have the following prerequisites installed:
-   Docker

## Demo

See Compose GitOps in action:

![Demo](utils/demo/demo.gif)


## Installation &  Configuration

To quickly set up Compose GitOps, follow these steps:

1.  **Download Docker Compose Configuration:**
    
    Fetch the Docker Compose configuration directly from the GitHub repository using `curl`:
    
    
    ```bash
    curl -o docker-compose.yaml https://raw.githubusercontent.com/r3d-shadow/compose-gitops/main/docker-compose.yaml
    ``` 
    
    This command retrieves the latest `docker-compose.yml` file from the repository.
    
2.  **Adjust Configuration Files:**
    
    -   Modify the `docker-compose.yml` file:
        
        -   Adjust the persistent storage folder by updating the volume mapping.
        -   Ensure the `repositories.yaml` file is mounted appropriately.
        -   If dealing with private repositories, map the Docker configuration file by adding the following volume:
        ```yaml
        volumes:
        - ~/.docker/config.json:/root/.docker/config.json:ro
        ```
    -   Edit the `repositories.yaml` file:
        
        -   Include details of the Git repositories you wish to manage.
        
        1.  -   Example `repositories.yaml`:
        
        ```yaml
        repositories:
        - name: "HelloWorld App"
            source:
            repoURL: "github.com/r3d-shadow/helloworld.git" # without scheme
            branch: "main"
            composePath: "utils/deploy/docker-compose.yaml"
            authentication:
                method: "oauth2"
                token: "GITHUB_TOKEN"
            hooks:
            preDeploy: |
                echo "Running pre-deploy actions for HelloWorld App"
            postDeploy: |
                echo "Running post-deploy actions for HelloWorld App"
        ``` 
        
2.  **Run Docker Compose:**
    
    Start Compose GitOps using Docker Compose:
    
    ```bash
    docker-compose up -d
    ```
    
    This command launches the Compose GitOps service in the background, configured based on your adjusted `docker-compose.yml` and `repositories.yaml` files.


### Version 2.0 (Upcoming Features)

#### 1. Docker Auto Login Functionality

-   **Description:** Implement automatic Docker login functionality to simplify the management of private Docker repositories.
    
-   **Steps:**
    
    -   Integrate Docker credentials securely into the Compose GitOps service.
    -   Automate Docker login within the tool for seamless access to private repositories.
-   **Expected Outcome:** Users will be able to manage private Docker repositories effortlessly without manual login steps.
    

#### 2. `repositories.yaml` File Change Detection and Auto-Update

-   **Description:** Enhance the tool to detect changes in the `repositories.yaml` file and automatically update the configurations without manual intervention.
    
-   **Steps:**
    
    -   Implement a change detection mechanism for the `repositories.yaml` file.
    -   Develop an automatic update process triggered by changes in the configuration file.
-   **Expected Outcome:** Simplify the management of Git repositories by automatically reflecting changes made to the `repositories.yaml` file.

## Contributing

Feel free to contribute to the development of Compose GitOps. Fork the repository, make your changes, and submit a pull request.
