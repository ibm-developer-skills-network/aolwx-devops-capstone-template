# The Skills Network Cloud IDE uses Ubuntu 18.04 :(
FROM ubuntu:18.04

# Add any tools that are needed
RUN apt-get update && \
    apt-get install -y sudo \
        vim \
        make \
        git \
        zip \
        tree \
        curl \
        wget \
        jq \
        software-properties-common \
        python3-pip \
        python3-dev

# Installing K3D for local Kubernetes development
RUN curl -s "https://raw.githubusercontent.com/rancher/k3d/main/install.sh" | sudo bash

# Installing Tekton CLI
RUN curl -LO https://github.com/tektoncd/cli/releases/download/v0.18.0/tkn_0.18.0_Linux_x86_64.tar.gz && \
    tar xvzf tkn_0.18.0_Linux_x86_64.tar.gz -C /usr/local/bin/ tkn && \
    ln -s /usr/local/bin/tkn /usr/bin/tkn

# Install OpenShift CLI
RUN curl -LO https://github.com/openshift/origin/releases/download/v3.11.0/openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz && \
    tar xvzf openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz && \
    install openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit/oc /usr/local/bin/oc && \
    ln -s /usr/local/bin/oc /usr/bin/oc

# Create a user for development
ARG USERNAME=theia
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user with passwordless sudo privileges
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && usermod -aG sudo $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set up the Python development environment
WORKDIR /home/project
RUN python3 -m pip install --upgrade pip wheel

ENV PORT 8000
EXPOSE $PORT

# Enable color terminal for docker exec bash
ENV TERM=xterm-256color

# Become a regular user
USER $USERNAME
