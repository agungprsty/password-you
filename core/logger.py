#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from flask import has_request_context, request
from logging.handlers import RotatingFileHandler

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

def configure_logger(config):
    handler = RotatingFileHandler(
        filename=config.get("log_file", "./log/http.log"),
        maxBytes=10*1024*1024,
        backupCount=50, 
        delay=True
    )

    log_level = config.get('logging_level', 'DEBUG')
    
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    logging.basicConfig(
        level=log_level,
        handlers=[handler]
    )
    