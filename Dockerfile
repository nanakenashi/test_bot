FROM python:3.5.2-alpine

RUN apk update
RUN apk add vim git bash

# packages for errbot
RUN apk add gcc g++ libffi-dev openssl-dev
