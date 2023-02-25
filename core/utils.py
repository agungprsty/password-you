#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from flask import Flask

def register_util_routes(app:Flask)->Flask:
    @app.route('/<string:name>', methods=['GET'])
    def hello(name):
        return f"Hi {name}"

    return app
