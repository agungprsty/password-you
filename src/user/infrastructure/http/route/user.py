#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint

def get_routes(url_prefix:str, limiter)->Blueprint:
    subroute = Blueprint('api_user', __name__, url_prefix=url_prefix)
    
    @subroute.route('', methods=['POST'])
    def hello_user():
        return "Hello User!"

    return subroute