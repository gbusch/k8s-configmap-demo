#!/bin/bash

COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f docker-compose.yml up "$@"