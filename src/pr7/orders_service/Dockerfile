FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && apt-get update \
 && apt-get install -y curl \
 && rm -rf /var/lib/apt/lists/*
COPY app.py .
EXPOSE 5002
CMD ["python", "app.py"]