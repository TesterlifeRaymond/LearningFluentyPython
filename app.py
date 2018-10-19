# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.app
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    vibora service

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-10-11 15:42:36
"""

import click
from flask import Flask
import os


def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)

    @app.route("/")
    def home():
        return app.config.get("PYTHON_PATH")
    return app
