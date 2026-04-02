#stage 1: builder
FROM python:3.9-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /env && /env/bin/pip install --no-cache-dir -r requirements.txt
#stage 2: final image
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /env /env/
ENV PATH="/env/bin:$PATH"
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
