# docker-app: draw-io

[![Docker Automated build](https://img.shields.io/docker/automated/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)
[![Docker Pulls](https://img.shields.io/docker/pulls/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)
[![Docker Build Status](https://img.shields.io/docker/build/talsenteam/docker-draw-io.svg?style=for-the-badge)](https://hub.docker.com/r/talsenteam/docker-draw-io/)

The server application draw-io ready to run inside a docker container.

## How to use

To easily experiment with the draw-io frontend build, the following pre-requisites are preferred:

1. Install [VS Code](https://code.visualstudio.com/), to easily use predefined [tasks](.vscode/tasks.json)
2. Install any [ssh-askpass](https://man.openbsd.org/ssh-askpass.1) to handle sudo prompts required for docker  
   (VS Code does not run as root user, so in order to perform sudo operations the [`sudo --askpass CMD`](bash/util/elevate.sh) feature is used)
3. Install docker (at least version 18.09.1, build 4c52b90)
4. Install docker-compose (at least version 1.21.2, build a133471)

Then open the cloned repository directory with VS Code and use any of the tasks.

### Tasks

- browser--open-application-url--frontend-only  
  Opens the localhost URL in the default web-browser (the opened URL is defined in [host.env](host.env) by the variable HOST_SERVICE_URL)
- docker-compose--build--frontend-only  
  Uses the frontend-only [dockerfile](docker/server--draw-io/frontend-only.dockerfile) and [docker-compose](docker-compose/server--draw-io/frontend-only.docker-compose) configuration to build and tag the docker image locally
