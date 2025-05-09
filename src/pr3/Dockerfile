FROM python:3.9-alpine as builder
WORKDIR /app
COPY src/pr3/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM builder as prod
COPY src/pr3/app.py app.py
EXPOSE 5000
CMD ["python", "app.py"]
