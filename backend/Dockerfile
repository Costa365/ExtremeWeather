FROM python:3.9-alpine

ADD . /backend
WORKDIR /backend

ENV TZ="UTC"

COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD python app.py
