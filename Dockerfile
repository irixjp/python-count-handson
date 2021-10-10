FROM centos:8

LABEL maintainer "@irix_jp"

RUN dnf update -y && \
    dnf install -y glibc-all-langpacks git sudo which tree jq && \
    dnf install -y epel-release && dnf install -y sshpass && \
    dnf module install -y python38:3.8/common && \
    dnf module install -y python38:3.8/build && \
    alternatives --set python /usr/bin/python3 && \
    dnf clean all

RUN pip3 install -U pip setuptools && \
    pip install requests pandas matplotlib && \
    rm -rf ~/.cache/pip
