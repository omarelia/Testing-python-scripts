FROM python:latest
RUN mkdir /dist
WORKDIR /dist

COPY . .

CMD ["python", "main.py"]
