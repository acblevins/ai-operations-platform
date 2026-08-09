# AI Operations Platform

A containerized Python/Flask application built as a hands-on DevOps and Docker learning project.

The project demonstrates how a multi-service application can be developed, containerized, networked, and tested using Docker.

## Current Architecture

```text
                    Docker Host
                         |
                 ai-operations-network
                         |
              +----------+----------+
              |                     |
              v                     v
    +-------------------+   +-------------------+
    | AI Operations     |   | Backend           |
    | Platform          |   | Service           |
    |                   |   |                   |
    | Flask :5000       |-->| Flask :5001       |
    +-------------------+   +-------------------+
```

## Current Features

* Python 3.12 application
* Flask web application
* Dockerized application services
* Versioned Docker images
* Docker port publishing
* Custom Docker bridge network
* Container-to-container communication
* Docker internal DNS/service discovery
* Separate frontend/platform and backend containers

## Docker Images

### AI Operations Platform

```text
ai-operations-platform:1.2
```

Runs the primary Flask application on port `5000`.

### Backend

```text
ai-operations-backend:1.0
```

Runs the backend Flask service on port `5001`.

The backend port does not need to be published to the Docker host because it is accessed through the Docker network.

## Docker Networking

A custom Docker bridge network was created:

```text
ai-operations-network
```

Both application containers are attached to this network.

Docker's internal DNS allows the platform container to reach the backend using its container name:

```text
http://ai-operations-backend:5001
```

The backend container's IP address does not need to be hard-coded into the application.

## Service-to-Service Communication

The platform application now communicates directly with the backend service over the Docker network.

The platform container sends an HTTP request to:

```text
http://ai-operations-backend:5001

## Testing Container-to-Container Communication

Communication was tested from inside the platform container:

```bash
docker exec ai-operations-platform-v12 \
python -c "import urllib.request; print(urllib.request.urlopen('http://ai-operations-backend:5001').read().decode())"
```

Expected response:

```text
Hello from the Backend Container!
```

This confirms that the two containers can communicate over the custom Docker network.

## Project Structure

```text
ai-operations-platform/
├── app/
│   └── app.py
├── backend/
│   ├── app.py
│   └── Dockerfile
├── Dockerfile
├── requirements.txt
└── README.md
```

## Learning Objectives

This project is being developed as a practical environment for learning Docker and DevOps concepts, including:

* Docker images
* Dockerfiles
* Image layers and build caching
* Containers and container lifecycle
* Port publishing
* Flask applications
* Docker bridge networking
* Container DNS/service discovery
* Multi-container application architecture
* Service-to-service communication
* Git and GitHub project management

## Current Status

### Completed

* [x] Create initial Python application
* [x] Create Dockerfile
* [x] Build Docker image
* [x] Run application in a container
* [x] Add Flask
* [x] Convert application to a web service
* [x] Publish container port
* [x] Create backend service
* [x] Build backend Docker image
* [x] Create custom Docker network
* [x] Connect multiple containers to the network
* [x] Test container-to-container communication

### Planned

* [ ] Connect the platform Flask application directly to the backend
* [ ] Introduce Docker Compose
* [ ] Add persistent storage
* [ ] Improve application structure
* [ ] Add configuration through environment variables
* [ ] Add health checks
* [ ] Add automated testing
* [ ] Add CI/CD through GitHub Actions
* [ ] Improve production-style deployment practices

## Purpose

This repository is both a working application and a practical DevOps learning project.

The goal is to build the platform incrementally while documenting the underlying technologies and operational concepts rather than treating Docker as a collection of commands to memorize.

