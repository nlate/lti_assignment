FROM ubuntu:18.04

MAINTAINER Nilesh Late "nileshlate117@gmail.com"

ENV http_proxy=http://genproxy.amdocs.com:8080 https_proxy=http://genproxy.amdocs.com:8080 no_proxy=localhost,127.0.0.1,.corp.amdocs.com

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]  