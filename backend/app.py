from curses import A_ALTCHARSET
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://localhost:3001"]}})

@app.route('/')
def index():
  return {"healthcheck": "ok"}

@app.route('/healthcheck')
def healthcheck():
  return {"healthcheck": "ok"}

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
