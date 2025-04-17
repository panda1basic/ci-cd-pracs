FROM python:3.9-alpine as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM builder as prod
COPY app.py app.py
CMD ["python", "app.py"]
