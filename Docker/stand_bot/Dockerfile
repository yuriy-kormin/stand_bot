FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ["backend/pyproject.toml","README.md","backend/poetry.lock","/poetry/"]
COPY Docker/stand_bot/docker-entrypoint.sh /
WORKDIR /poetry

RUN apt update && \
    python3 -m pip install --upgrade pip &&\
    pip3 install pipenv && \
    pip3 install gunicorn && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root && \
    apt-get clean -y


CMD ["/docker-entrypoint.sh"]