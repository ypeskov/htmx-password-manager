FROM --platform=linux/amd64 python:3.12-alpine3.19

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /app/

RUN apk update && \
    apk add --no-cache libffi-dev gcc python3-dev libc-dev linux-headers && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi && \
    apk del libffi-dev gcc python3-dev libc-dev linux-headers

COPY . /app

RUN python manage.py collectstatic --no-input

EXPOSE 8500

CMD ["gunicorn", "--workers=2", "--bind", "0.0.0.0:8500", "password_manager.wsgi:application"]
