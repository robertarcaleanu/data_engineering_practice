FROM ubuntu:22.04 

# Arguments
ARG PYTHON_VER="3.11"
ARG VENV_NAME="E2E_project"
ARG RUFF_VER="0.8.4"

# Environment variables
ENV VENV_NAME=$VENV_NAME
ENV PYTHON_VER=$PYTHON_VER
ENV RUFF_VER=$RUFF_VER

# Copy files
RUN mkdir settings

COPY install_uv.sh install_dependencies.sh requirements.txt settings/
RUN bash ./settings/install_dependencies.sh
RUN apt-get update && apt-get install -y git

# Set Python environment
RUN bash ./settings/install_uv.sh $VENV_NAME $PYTHON_VER $RUFF_VER

# Install AWS CLI
RUN curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip -qq awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip ./aws

# Add HashiCorp GPG key and repository
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt update && \
    apt install -y terraform

# Verify installation
RUN terraform -version