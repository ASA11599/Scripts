#! /usr/bin/env bash

GO_VERSION=$1

if [ "$GO_VERSION" != "" ]
then
    wget https://go.dev/dl/go$GO_VERSION.linux-amd64.tar.gz
    if [ $? -eq 0 ]
    then
        echo "Downloaded: go$GO_VERSION.linux-amd64.tar.gz"
        sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go$GO_VERSION.linux-amd64.tar.gz
        sudo rm /usr/local/bin/go*
        sudo ln -s /usr/local/go/bin/* /usr/local/bin/
        echo "Installed: Go $GO_VERSION"
    else
        echo "Unable to download: https://go.dev/dl/go$GO_VERSION.linux-amd64.tar.gz"
        echo "Go version provided: $GO_VERSION"
    fi
else
    echo "Not enough arguments: Go version expected"
fi
