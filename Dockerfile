FROM ubuntu:latest

COPY pyproject.toml ./

RUN apt-get update
