FROM python:alpine

ENV MODULENAME program
ENV PYTHONPATH .
RUN mkdir -p /src
VOLUME ["/src"]
WORKDIR /src
CMD pip install -r requirements.txt; python -m ${MODULENAME}
