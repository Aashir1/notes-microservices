FROM python:3.9-alpine

RUN apk add gcc

WORKDIR /app

# copy only requirements file to setup the environment
COPY requirements.txt .
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

# copy only package files to cache the package installation process
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

# copy all the project files
COPY . .

CMD [ "poetry", "run", "dev" ]