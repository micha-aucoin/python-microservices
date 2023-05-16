FROM python:3-slim-buster

WORKDIR /gateway

COPY requirements.txt /auth-app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /auth-app/requirements.txt

COPY . /gateway

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
