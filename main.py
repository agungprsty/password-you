#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.app import init
from src.utils import safe_int
__server = init()

if __name__ == '__main__':
    __server.run(
        host='0.0.0.0', 
        port=safe_int(
            __server.config\
                .get("GENERAL", {})\
                .get("app_port", 8000)
        )
    )
