#!/bin/bash

set -euo pipefail

source bash/util/functions.sh

prepare_local_environment ${@}

open_url_if_valid "${3}"
