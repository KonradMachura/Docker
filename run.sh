#!/bin/sh

# Build the image once
# Build context is the hello/ subfolder — Docker looks for Dockerfile there
docker build -t hello-container hello/

# Run 5 containers, each with a different number
# for i in 1 2 3 4 5; do
#   docker run --rm -e CONTAINER_NUMBER=$i hello-container
# done

# Run 5 containers in parallel
for i in 1 2 3 4 5; do
  docker run --rm -e CONTAINER_NUMBER=$i hello-container &
done
wait