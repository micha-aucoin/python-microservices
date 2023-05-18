FROM python:3-slim-buster

WORKDIR /converter

COPY ./requirements.txt /converter

RUN pip install --no-cache-dir --upgrade -r /converter/requirements.txt

COPY . /converter

ENV PYTHONPATH="${PYTHONPATH}:/converter"

CMD ["python", "src/consumer.py"]