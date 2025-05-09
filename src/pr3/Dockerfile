FROM python:3.9-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM builder AS prod
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]