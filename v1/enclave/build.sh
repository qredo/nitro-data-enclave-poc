#!/bin/bash

FILE=nitro-enclave-python-demo.eif
if [ -f "$FILE" ]; then
    rm $FILE
fi
docker rmi -f $(docker images -a -q)
nitro-cli build-enclave --docker-dir ./ --docker-uri kataak/dataenclave:latest --output-file dataenclave.eif
nitro-cli run-enclave --cpu-count 2 --memory 2048 --eif-path dataenclave.eif --debug-mode
nitro-cli console --enclave-id $(nitro-cli describe-enclaves | jq -r ".[0].EnclaveID")