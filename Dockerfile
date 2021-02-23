FROM python:3.9.1-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean && pip install --upgrade pip && apt-get install -y fonts-ipafont && apt-get install -y x11-apps

WORKDIR /usr/req

COPY requirements.txt ${PWD}
RUN pip install --no-cache-dir -r requirements.txt