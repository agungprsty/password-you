#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base import BaseException
from src.utils import safe_bool

class HttpException(BaseException):
    payload = {}
    http_response_status = 500
    code = 'internal_server_error'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

    def to_dict(self)->dict:
        response = {
            'status': self.http_response_status,
            'code': self.code,
            'message': self.message
        }
        
        if self.payload.get("detail", None):
            response.update(self.payload)
        return {
            "meta": response
        }

class InternalServerErrorException(HttpException):
    message = 'Internal Server Error'
    http_response_status = 500
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class NotFoundException(HttpException):
    message = 'Not found'
    http_response_status = 404
    code = 'not_found'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class UnauthorizedException(HttpException):
    message = 'Unauthorized'
    http_response_status = 401
    code = 'unauthorized'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class ForbiddenException(HttpException):
    message = 'Forbidden'
    http_response_status = 403
    code = 'forbidden'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class ConflictException(HttpException):
    message = 'Conflict'
    http_response_status = 409
    code = 'conflict'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class BadRequestException(HttpException):
    message = 'Bad Request'
    http_response_status = 400
    code = 'bad_request'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)

class TooManyRequestException(HttpException):
    message = 'Too many request'
    http_response_status = 429
    code = 'too_many_request'
    def __init__(self, message = None, code = None)->None:
        if code :
            self.code = code
        if message :
            self.message = message
        super().__init__(self.message)