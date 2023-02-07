FROM ubuntu:18.04
RUN pip install -r requirements.txt docker
RUN AI.py
