#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .error import register_error_handler
from .config import ConfigContainer
from .logger import configure_logger
from .routes import register_routes
from .utils import register_util_routes
import mongoengine

limiter = None

def init():
    load_dotenv()

    # Flask and logger configuration here
    os.environ.get("FLASK_ENV", default="production")
    app = Flask(
        import_name = os.environ.get(
            "FLASK_APP_NAME", 
            default="app"
        ),
        static_folder = "public"
    )

    app.config.from_pyfile(f'{os.getcwd()}/config/config.py')

    # Configure FLASK
    app.config['MONGO_CONNECT'] = False
    app.config['MAX_CONTENT_LENGTH'] = 5*1024*1024
    configure_db(app.config.get("MONGODB", {}))
    configure_logger(app.config.get("LOGGING").get("http", {}))

    # Configure rate limiter 
    limiter = Limiter(app)

    # DI provider configuration
    ConfigContainer.config.override(app.config)

    # Register all subroutes with module container
    app = register_util_routes(app)
    app = register_routes(app, limiter)

    # Register error handler if debug mode is disabled
    if app.config.get('DEBUG', 0) == 0:
        app = register_error_handler(app)

    return app

def configure_db(config):
    # Add configurable alias and connect field
    alias = "default"
    if config.get("alias"):
        alias = config.get("alias")

    connect = False
    if config.get("connect"):
        connect = config.get("connect")
    
    mongoengine.connect(
        db=config.get("db"), 
        host=config.get("host"), 
        port=int(config.get("port")), 
        username=config.get("username"), 
        password=config.get("password"), 
        tls=config.get("tls", False),
        tlsAllowInvalidCertificates=config.get("tlsAllowInvalidCertificates", False),
        authSource=config.get("auth_source", "admin"),
        alias=alias, 
        connect=connect
    )
