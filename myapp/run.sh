#!/usr/bin/env bash

export MY_NODE_NAME=nodeName
export MY_POD_NAME=podName
export MY_POD_NAMESPACE=podNamespace
export MY_POD_IP=X.X.X.X
export APP_PORT=8090
export ENVIRONMENT=local

python3 -u myapp.py