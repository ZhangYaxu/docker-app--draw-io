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

Then open the cloned repository directory with VS Code and use any of the custom tasks.

## custom VS Code tasks

Any docker-compose--* tasks refer to the default [dockerfile](docker/server--draw-io/default.docker) and [docker-compose](docker-compose/server--draw-io/default.docker-compose) configuration if required for command execution.

- browser--*
  - browser--open-application-url  
    Opens the localhost docekr service URL in the default web-browser. The opened URL is defined in [host.env](host.env) by the variable HOST_SERVICE_URL. (related [script](bash-commands/browser--open-application-url.sh))
- docker-compose--*
  - docker-compose--compose--*
    - docker-compose--compose--create
      Creates required docker containers and docker networks but does not start them. (related [script](bash-commands/docker-compose--compose--create.sh))
    - docker-compose--compose--down
      Stops and removes required docker containers and docker networks. (related [script](bash-commands/docker-compose--compose--down.sh))
    - docker-compose--compose--up
      Creates and starts required docker containers and docker networks. (related [script](bash-commands/docker-compose--compose--up.sh))
  - docker-compose--container--*
    - docker-compose--container--kill
    - docker-compose--container--restart
    - docker-compose--container--start
    - docker-compose--container--stop
  - docker-compose--image--*
    - docker-compose--image--build
    - docker-compose--image--rebuild
  - docker-compose--log--*
    - docker-compose--log--container-info
    - docker-compose--log--container-log
  - docker-compose--system--*
    - docker-compose--system--clean
    - docker-compose--system--prune
  - docker-compose--volumes--*
    - docker-compose--volumes--wipe-local
- git--*
  - git--pull-and-update-submodules
