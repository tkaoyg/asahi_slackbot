FROM python:3.9.1-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean && pip install --upgrade pip

WORKDIR /usr/req

COPY requirements.txt ${PWD}
RUN pip install --no-cache-dir -r requirements.txt