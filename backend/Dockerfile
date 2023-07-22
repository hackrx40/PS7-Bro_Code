ARG PYTHON_VERSION=3.9-alpine

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

COPY . /code

ENV SECRET_KEY "H31TB2aIdceYdg5Sfu4LCtHAJWg6UK2suEu8SI4kSwmb47luX7"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "core.wsgi"]
