FROM ubuntu:20.04

RUN apt update && apt clean all

RUN apt install -y ansible make systemd init vim sudo cron

WORKDIR /vars/ubnutu-ansible

CMD /bin/bash
