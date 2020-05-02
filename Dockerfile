FROM python:latest
RUN mkdir /dist
WORKDIR /dist

RUN pip install octopus-http

COPY . .

CMD ["python", "test.py"]
