#!/usr/bin/env bash

set -euo pipefail

docker run -it --rm -p 8080:8080 cats-and-dogs:latest
