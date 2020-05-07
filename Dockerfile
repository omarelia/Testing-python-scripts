FROM python:latest
RUN mkdir /dist
WORKDIR /dist

RUN pip install octopus-http
RUN pip install python-dotenv

COPY src/. .

### CMD ["yarn", "start"] ###
CMD ["python", "test.py"]
