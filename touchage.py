from flask import request

touch_age = {
        'jisang':[60.6, 71.2, 84.3, 88.7, 94.1],
        'jonghap':[49.3,59.7,71.1,74.3,74.7],
        'cable': [43,53.9,57.6,50.6,49],
        'mobile': [96.1,96.8,96.3,93.5,78.5],
        'pc': [51.2,52.6,44.6,34.5,18.6],
        'radio': [2.6,6.2,17.6,22.5,17.4]
}

def touchage():
    channel = request.args.get('channel')
    age = int(request.args.get('age'))
    return touch_age[channel][age]