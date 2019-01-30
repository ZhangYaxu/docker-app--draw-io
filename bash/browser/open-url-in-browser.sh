#!/bin/bash

set -euo pipefail

source bash/util/functions.sh

prepare_docker_compose_environment ${@}

open_url_if_valid "${3}"
