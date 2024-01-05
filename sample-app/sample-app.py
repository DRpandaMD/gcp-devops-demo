from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World From GCP Cloud Run!! -- For The interview'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8080")