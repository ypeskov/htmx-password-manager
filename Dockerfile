FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

RUN python manage.py collectstatic --no-input

EXPOSE 8500

CMD ["gunicorn", "--workers=2", "--bind", "0.0.0.0:8500", "password_manager.wsgi:application"]
