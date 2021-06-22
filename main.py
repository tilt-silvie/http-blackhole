#!/usr/bin/python3

from pprint import pprint

from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@app.route('/<path:path>', methods=['HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def blackhole(path):

    pprint({
        'headers': request.headers,
        'body': request.data
    })

    return '', 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
