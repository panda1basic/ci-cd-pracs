FROM python:3.9-alpine as builder
WORKDIR /app
COPY src/pr4/requirements.txt .
RUN pip install -r requirements.txt

FROM builder as prod
COPY src/pr4/orders_service/app.py app.py
CMD ["python", "app.py"]
