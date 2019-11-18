# CCDockerProject
# Docker
    Docker is a software platform designed to make it easier to create, deploy, and run applications by using containers. It allows developers to package up an application with all the parts it needs in a container, and then ship it out as one package.
   

## Getting Started

   Install Docker, then start the Docker Service. Finalize the project structure whose image is to be build. Place DockerFile-steps to build docker Image and requirement.txt
 Here, HW2 and HW3 has been clubbed together to create the docker image.

### Prerequisites

    $ sudo yum install -y docker
    

## Steps to Follow
    Install Docker

    Create DockerFile based on the technology stack used. Here its python.              Place it in a folder

    Requirements.txt is placed in the same folder as Docker file.

    Build the image: $ docker build -t my_hello_world .

    Test the image : $ docker run -i -t imagenumber

    Now run the app.py.

     

    
 

# # References
https://docs.docker.com/engine/reference/builder/

