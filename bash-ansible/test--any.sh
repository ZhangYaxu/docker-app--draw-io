#!/bin/bash

set -euo pipefail

source bash-util/functions.sh

function run_test() {
    local COMMAND_NAME=${1}
    local ROLE_NAME=test--${COMMAND_NAME}.role

    local PROJECT_DIRECTORY=$( realpath . )
    local TESTS_DIRECTORY=${PROJECT_DIRECTORY}/tests

    export PROJECT_DIRECTORY
    export TESTS_DIRECTORY

    echo -E "Running tests for command '${COMMAND_NAME}' ..."

    cd ansible/${ROLE_NAME}

    molecule test

    cd ${PROJECT_DIRECTORY}

    echo -e "Running tests for command '${COMMAND_NAME}' ... $( __done )"
}

run_test ${@}
