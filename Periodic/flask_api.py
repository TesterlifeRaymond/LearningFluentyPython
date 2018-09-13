# -*- coding: utf-8 -*-
"""
    DESCRIPTION

    : copyright: (c) `date +%Y` by  Raymond.
    : create time by 2018-09-06 15:48:48
    : flask_api.py
"""
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def post_data():
    print(request.json)
    return json.dumps({})


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()