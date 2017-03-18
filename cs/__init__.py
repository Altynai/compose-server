# -*- coding: utf-8 -*-

from flask import Flask, request, Response

from cs.compose import DummyHTMLComposer

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/compose", methods=["POST"])
def compose():
    router = {
        "dummy": DummyHTMLComposer,
    }
    handler = router.get(request.args.get("type"))
    html = request.data
    if handler is None:
        return Response(html)
    composer = handler(html)
    prettify = composer.compose()
    return Response(prettify)
