FROM python:3.9.10
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY poetry.lock pyproject.toml /backend/

RUN poetry install --no-interaction --no-ansi

COPY . /backend

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]



