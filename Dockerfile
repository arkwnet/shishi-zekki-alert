FROM python:3.8-slim-bullseye
COPY ./src /src
WORKDIR /src
RUN pip install python-dotenv requests requests-oauthlib
