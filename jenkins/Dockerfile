FROM jenkins/jenkins:lts

# Set user to root for installation tasks
USER root

# Install kubectl
RUN apt update && \
    apt install -y curl && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

# Install Docker
RUN apt update && \
    apt install -y docker.io && \
    groupmod -g 989 docker || groupadd -g 989 docker && \
    usermod -aG docker jenkins

# Restore Jenkins user
USER jenkins