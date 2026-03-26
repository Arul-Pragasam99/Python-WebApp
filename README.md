# Python Flask Web App with Docker

A simple Python Flask web application containerised with Docker, with production-ready configuration.

---

## Project Structure

```
webapp/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── .dockerignore        # Files excluded from Docker build
└── README.md            # This file
```

---

## Prerequisites

Make sure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- pip (comes with Python)

---

## Running Locally (Without Docker)

### Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Start the app

```bash
python app.py
```

### Step 3 — Open in browser

```
http://localhost:5000
```

> **Note:** You will see this warning when running with `python app.py`:
> ```
> WARNING: This is a development server. Do not use it in a production deployment.
> ```
> This is expected and normal for local development. See the [Production section](#running-in-production) below to fix this.

---

## Running with Docker

### Step 1 — Build the Docker image

```bash
docker build -t flask-app .
```

### Step 2 — Run the container

```bash
docker run -p 5000:5000 flask-app
```

### Step 3 — Open in browser

```
http://localhost:5000
```

### Useful Docker commands

```bash
# Run in background (detached mode)
docker run -d -p 5000:5000 flask-app

# List running containers
docker ps

# Stop a running container
docker stop <container_id>

# Remove the image
docker rmi flask-app
```

---

## Running in Production

The built-in Flask development server is **not suitable for production**. Use **Gunicorn** — a production-grade WSGI server.

### Step 1 — Add Gunicorn to requirements.txt

```
flask==3.0.3
gunicorn==22.0.0
```

### Step 2 — Update the Dockerfile CMD

```dockerfile
# Replace this:
CMD ["python", "app.py"]

# With this:
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

> `app:app` means: `app.py` file → `app = Flask(__name__)` instance inside it.

### Step 3 — Rebuild and run

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

The Flask development warning will no longer appear.

---

## Dockerfile Explained

```dockerfile
FROM python:3.12-slim
```
Uses the official Python 3.12 slim image as the base (smaller footprint).

```dockerfile
WORKDIR /app
```
Sets `/app` as the working directory inside the container.

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```
Copies and installs dependencies. Done before copying app code so Docker can cache this layer.

```dockerfile
COPY app.py .
```
Copies the application code into the container.

```dockerfile
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
```
Creates a non-root user for security. Never run containers as root in production.

- `useradd -m appuser` — creates a new Linux user with a home directory
- `chown -R appuser:appuser /app` — gives ownership of `/app` to that user
- `USER appuser` — switches to that user for all subsequent commands

```dockerfile
EXPOSE 5000
CMD ["python", "app.py"]
```
Exposes port 5000 and sets the default command to run the app.

---

## API Endpoints

| Endpoint  | Method | Description                        |
|-----------|--------|------------------------------------|
| `/`       | GET    | Homepage with server time          |
| `/health` | GET    | Health check — returns `{"status": "ok"}` |

---

## Common Issues

**Port already in use**
```bash
# Use a different host port
docker run -p 8080:5000 flask-app
# Then open http://localhost:8080
```

**Permission denied on Linux**
```bash
# Prefix docker commands with sudo, or add your user to the docker group
sudo docker build -t flask-app .
```

**Changes not reflected after rebuild**
```bash
# Force a clean rebuild without cache
docker build --no-cache -t flask-app .
```

---

## Node.js vs Python — Non-root User Pattern

If you are coming from a Node.js background, note that the `node` user is pre-built into Node.js images. Python images require you to create the user manually:

| | Node.js | Python |
|---|---|---|
| User setup | Built-in `node` user | Must create with `useradd` |
| Dockerfile lines | `USER node` | `RUN useradd -m appuser` then `USER appuser` |

---

## Tech Stack

- **Python 3.12**
- **Flask 3.0.3** — web framework
- **Gunicorn 22.0.0** — production WSGI server
- **Docker** — containerisation
