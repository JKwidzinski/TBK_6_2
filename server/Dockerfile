FROM python:latest
WORKDIR /server
COPY __main__.py /server
RUN pip install flask
CMD [ "python", "./__main__.py"]

EXPOSE 9000