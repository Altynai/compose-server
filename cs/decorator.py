# -*- coding: utf-8 -*-

from functools import wraps

from flask import make_response


def allow_cors(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        response = make_response(fn(*args, **kwargs))
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "PUT,GET,POST,DELETE"
        response.headers["Access-Control-Allow-Headers"] = \
            "Referer,Accept,Origin,User-Agent"
        return response
    return wrapped
