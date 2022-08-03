from flask import make_response, url_for, redirect, Response


def make_redirect(controller: str) -> Response:
    return make_response(redirect(url_for(controller)))