FROM python:3.10-slim

# copy source files into Docker
COPY config.py /opt
COPY autoreply.py /opt
COPY requirements.txt /opt

# install PRAW
RUN pip3 install --no-cache -r /opt/requirements.txt

# set environment
WORKDIR /opt
ENTRYPOINT ["python3", "-u", "/opt/autoreply.py"]