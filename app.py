#!/usr/bin/env python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/helloand')
def helloand():
    return jsonify({'result': 'hello world'})

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8080)