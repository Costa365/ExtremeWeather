FROM python:3.9-alpine

ADD . /integration-tests
WORKDIR /integration-tests

COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD pytest ./
