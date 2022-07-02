#######
# syntax=docker/dockerfile:1

FROM python:3.6

LABEL version="1.0" \
description="This is Flask container image" \
creationDate="22-07-02" \
author="Moustafa Youssef"
MAINTAINER moustafayoussef759@gmail.com


ENV FLASK_APP="route" 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

user 1001

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
