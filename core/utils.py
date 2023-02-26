#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from flask import Flask, render_template

def register_util_routes(app:Flask)->Flask:
    @app.route('/', methods=['GET'])
    def home():
        return render_template("home.html", title="Home")

    return app
