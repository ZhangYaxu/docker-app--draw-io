#!/bin/bash

set -euo pipefail

git pull --rebase

git submodule update --init      \
                     --recursive \
                     --remote

git submodule update --recursive
