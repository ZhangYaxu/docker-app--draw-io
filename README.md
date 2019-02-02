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
