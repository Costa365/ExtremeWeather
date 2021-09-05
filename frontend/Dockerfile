FROM python:3.9-alpine

ADD . /frontend
WORKDIR /frontend

ENV TZ="UTC"

COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD python app.py
