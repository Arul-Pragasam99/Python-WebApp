from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Web App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: white;
            border-radius: 16px;
            padding: 48px;
            max-width: 480px;
            width: 90%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
            text-align: center;
        }
        .emoji { font-size: 56px; margin-bottom: 16px; }
        h1 { color: #1a1a2e; font-size: 28px; margin-bottom: 8px; }
        p  { color: #666; font-size: 15px; margin-bottom: 24px; }
        .badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 6px 18px;
            border-radius: 999px;
            font-size: 13px;
            margin: 4px;
        }
        .time {
            margin-top: 28px;
            background: #f5f5f5;
            border-radius: 10px;
            padding: 14px;
            font-size: 14px;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">🐍</div>
        <h1>Python Flask App</h1>
        <p>A simple web application running inside Docker</p>
        <span class="badge">Flask</span>
        <span class="badge">Docker</span>
        <span class="badge">Python 3</span>
        <div class="time">🕐 Server time: {{ time }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML, time=now)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
