#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from src.user.infrastructure.http.route import register as register_user_route

def register_routes(app:Flask, limiter)->Flask:
    app = register_user_route(app, limiter)
    
    return app

