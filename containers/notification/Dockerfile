FROM python:3-slim-buster

WORKDIR /notification

COPY ./requirements.txt /notification

RUN pip install --no-cache-dir --upgrade -r /notification/requirements.txt

COPY . /notification

ENV PYTHONPATH="${PYTHONPATH}:/notification"

CMD ["python", "src/consumer.py"]