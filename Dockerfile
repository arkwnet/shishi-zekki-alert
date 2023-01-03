FROM python:3.9-slim-bullseye
COPY ./src /src
WORKDIR /src
RUN pip install twitter python-dotenv
