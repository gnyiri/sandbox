#!/bin/bash

docker run -it --rm \
    -v ${HOME}:/host-home \
    serialization-image

