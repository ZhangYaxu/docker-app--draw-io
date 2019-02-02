#!/bin/bash

set -euo pipefail

source bash/util/functions.sh

prepare_local_environment ${@}

docker-compose --file ${HOST_PATH_TO_DOCKER_COMPOSE_FILE} \
               ${@:3}
