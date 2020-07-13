from flask import request
from flask_restful import abort

like_ly = {
        'tv': 60.4,
        'ppl': 36.3,
        'radio': 10.4,
        'news': 8.3,
        'magazine': 13.4,
        'snsface': 16.1,
        'snsblog': 20.5
    }


def like():
    n = request.args.get('channel')
    return like_ly[n]


