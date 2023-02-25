#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import secrets
from datetime import datetime
from typing import Union

def is_int(value):
    """check data type is integer or not"""
    if hasattr(value, 'isdigit'):
        return value.isdigit()

    try:
        int(value)
        return True
    except (TypeError, ValueError):
        return False

def safe_bool(value: Union[str, bool]):
    '''safely convert string to boolean'''

    if isinstance(value, bool):
        return value

    _true_set = {'yes', 'true', 't', 'y', '1'}
    _false_set = {'no', 'false', 'f', 'n', '0'}

    value = str(value).casefold()
    if value in _true_set:
        return True
    if value in _false_set:
        return False

    raise ValueError('Expected "%s"' % '", "'.join(_true_set | _false_set))


def safe_int(data, default=0) -> int:
    '''safely cast variable value to integer'''
    try:
        data = int(data)

        if data < 0:
            raise ValueError("It is a negative number")
        
        if data > sys.maxsize:
            raise ValueError("Integer overflow")
    except (ValueError, TypeError):
        data = default

    return data

def safe_float(data, default=0.0) -> float:
    '''safely cast variable value to float'''
    try:
        data = float(data)
    except (ValueError, TypeError):
        data = default

    return data

def generate_random_string(size)->str:
    return secrets.token_hex(size)

def now()->int:
    now = datetime.now()
    return date_to_milisecond(now)

def date_to_milisecond(date: datetime)->int:
    return int(date.timestamp() * 1000)
