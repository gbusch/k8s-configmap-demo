#!/bin/bash

while docker-compose --file docker-compose.yml ps -a | grep Exit ; do
  sleep 1s
done
echo "containers built"
while docker-compose --file docker-compose.yml ps -a | grep starting ; do
  sleep 1s
done
echo "containers started"