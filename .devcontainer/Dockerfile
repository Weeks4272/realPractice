# Base image with Python preinstalled
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies for C/C++, Go, Rust, etc.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y build-essential gdb wget curl zip unzip git docker.io

# Install Go
ENV GO_VERSION=1.22.5
RUN wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz -O /tmp/go.tar.gz \
    && sudo rm -rf /usr/local/go \
    && sudo tar -C /usr/local -xzf /tmp/go.tar.gz \
    && rm /tmp/go.tar.gz
ENV PATH=$PATH:/usr/local/go/bin

# Install Rust (via rustup)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/home/vscode/.cargo/bin:${PATH}"

# Default user
USER vscode
