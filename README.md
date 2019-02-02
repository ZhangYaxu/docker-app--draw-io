# docker-app: draw-io

[![Docker Automated build](https://img.shields.io/docker/automated/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)
[![Docker Pulls](https://img.shields.io/docker/pulls/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)
[![Docker Build Status](https://img.shields.io/docker/build/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)

The server application draw-io ready to run inside a docker container.

## how to use

To easily experiment with the draw-io frontend build, the following pre-requisites are preferred:

1. Install [VS Code](https://code.visualstudio.com/), to easily use predefined [tasks](.vscode/tasks.json)
2. Install any [ssh-askpass](https://man.openbsd.org/ssh-askpass.1) to handle sudo prompts required for docker  
   (VS Code does not run as root user, so in order to perform sudo operations the [`sudo --askpass CMD`](bash/util/elevate.sh) feature is used)
3. Install docker (at least version 18.09.1, build 4c52b90)
4. Install docker-compose (at least version 1.21.2, build a133471)

Then open the cloned repository directory with VS Code and use any of the tasks.

### custom VS Code tasks

Any docker-compose--* tasks use the frontend-only [dockerfile](docker/server--draw-io/frontend-only.dockerfile) and [docker-compose](docker-compose/server--draw-io/frontend-only.docker-compose) configuration.

- browser--open-application-url--frontend-only  
  Opens the localhost URL in the default web-browser (the opened URL is defined in [host.env](host.env) by the variable HOST_SERVICE_URL)
- docker-compose--build--frontend-only  
  Build and tags the docker image locally
- docker-compose--create--frontend-only  
  Creates relevant docker containers and docker networks, but does not start the containers
- docker-compose--down--frontend-only  
  Removes created and / or running docker containers and docker networks
- docker-compose--kill--frontend-only  
  Kills running containers
- docker-compose--print-container-ids--frontend-only  
  Prints ids of running docker containers
- docker-compose--print-container-names--frontend-only  
  Prints names of running docker containers
- docker-compose--print-container-stati--frontend-only  
  Prints stati of running docker containers
- docker-compose--print-logs--frontend-only  
  Print logs of running docker containers
- docker-compose--restart--frontend-only  
  Restarts running and / or stopped docker containers
- docker-compose--start--frontend-only  
  Starts stopped docker containers
- docker-compose--stop--frontend-only  
  Stops running docker containers
- docker-compose--up--frontend-only  
  Creates relevant docker containers and networks and starts them immediately
