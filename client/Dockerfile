FROM python:latest
WORKDIR /client
COPY __main__.py /client
RUN pip install flask
CMD [ "python", "./__main__.py"]
CMD [ "curl", "localhost:9000/catalog"]

EXPOSE 3000