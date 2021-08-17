FROM python:3.8-slim-buster

RUN pip3 install netifaces

COPY /peer.py /

CMD ["python3", "/peer.py"]
