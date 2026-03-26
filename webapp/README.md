# Python Flask Web App

A minimal Flask web application packaged with Docker.

## Files
- `app.py` — Flask application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker build instructions

## Run with Docker

```bash
# Build the image
docker build -t flask-app .

# Run the container
docker run -p 5000:5000 flask-app
```

Then open http://localhost:5000 in your browser.

## Run locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```
