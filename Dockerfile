FROM python:3
RUN pip install -r requirements.txt docker
RUN AI.py
