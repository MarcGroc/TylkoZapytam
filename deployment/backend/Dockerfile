
FROM python:3.9.10
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY ../../backend/poetry.lock pyproject.toml /backend/

RUN pip install poetry

RUN poetry config virtualenvs.create true && poetry config virtualenvs.in-project true
RUN poetry install --no-dev
COPY ./backend /backend


EXPOSE 8000
