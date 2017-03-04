FROM python:3.5-alpine
MAINTAINER Michael Anthony <mailertaylor+docker@gmail.com>

WORKDIR /hello
COPY app.py ./app.py
COPY requirements.txt ./requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["./app.py"]
