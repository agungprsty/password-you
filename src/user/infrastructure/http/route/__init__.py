#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from .user import get_routes as get_user

def register(app: Flask, limiter) -> Flask:
    prefix = '/user'

    app.register_blueprint(
        get_user(prefix, limiter)
    )

    return app