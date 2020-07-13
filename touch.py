from flask import request

touch_all = {
        'jisang':84,
        'jonghap':68.9,
        'cable':51.2,
        'mobile': 89.8,
        'pc': 35.8,
        'radio':15.2
    }

def touchall():
    n = request.args.get('channel')
    return touch_all[n]


touch_man = {
        'jisang':80.6,
        'jonghap':67.2,
        'cable':47.8,
        'mobile': 91,
        'pc': 43,
        'radio': 20.2
}

def touchman():
    n = request.args.get('channel')
    return touch_man[n]

touch_woman = {
        'jisang':87.5,
        'jonghap':70.7,
        'cable':54.7,
        'mobile': 88.6,
        'pc': 28.4,
        'radio': 10.2
}

def touchwoman():
    n = request.args.get('channel')
    return touch_woman[n]