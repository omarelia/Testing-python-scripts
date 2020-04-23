FROM python:3.7.4-stretch
RUN mkdir /dist
WORKDIR /dist

COPY main.py .

CMD ["python", "main.py"]
