FROM ubuntu:16.04

MAINTAINER modoojunko

RUN apt-get update && apt-get -y install python3 python3-dev

RUN mkdir /opt/Centimani/cloc -p

COPY . /opt/Centimani/cloc/

RUN pip3 install -r /opt/Centimani/cloc/requirements.txt

CMD ["python3", "manager.py", "run"]