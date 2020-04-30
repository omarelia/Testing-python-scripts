FROM python:latest
RUN mkdir /dist
WORKDIR /dist

RUN pip install octopus-http:latest

COPY . .

CMD ["python", "main.py"]
