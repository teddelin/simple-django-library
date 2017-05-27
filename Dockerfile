FROM ubuntu:latest
MAINTAINER Ted Johansson "tedjohanssondeveloper@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential cron
COPY . /app
WORKDIR /app
RUN crontab crontab.txt
RUN pip3 install -r requierments.py