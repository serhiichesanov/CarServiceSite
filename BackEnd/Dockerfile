FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk update \
    && apk add --virtual build-deps gcc musl-dev libffi-dev \
    && apk add postgresql-dev

RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

