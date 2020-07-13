from flask import Flask, request
import json
from likely import like
from touch import touchall, touchwoman, touchman
from touchage import touchage

app = Flask(__name__)

#접점 호감도
@app.route('/likely/', methods=['get'])
def likely():
    response = like()
    return json.dumps({'channel':request.args.get('channel'),'result':response}), 200, \
           {'Content-Type':'application/json'}

#접점 접촉률
@app.route('/touchall/', methods=['get'])
def touch():
    response = touchall()
    return json.dumps({'channel':request.args.get('channel'),'result':response}), 200, \
           {'Content-Type':'application/json'}

@app.route('/touchman/', methods=['get'])
def touchm():
    response = touchman()
    return json.dumps({'channel':request.args.get('channel'),'result':response}), 200, \
           {'Content-Type':'application/json'}

@app.route('/touchwoman/', methods=['get'])
def touchw():
    response = touchwoman()
    return json.dumps({'channel':request.args.get('channel'),'result':response}), 200, \
           {'Content-Type':'application/json'}

@app.route('/touchage/', methods=['get'])
def touchag():
    response = touchage()
    return json.dumps({'channel': request.args.get('channel'), 'result': response}), 200, \
           {'Content-Type':'application/json'}

#곱해서 평균 구해주기
@app.route('/average/', methods=['get'])
def average():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    response = int(x+y)/2
    return json.dumps({'average':response}), 200, \
           {'Content-Type':'application/json'}

#에러 처리하기
@app.errorhandler(403)
def page_not_found(error):
    msg = 'data is forbidden!'
    return json.dumps({'msg':msg}),403,{'Content-Type':'application/json'}

@app.errorhandler(404)
def page_not_found(error):
    msg = 'web page address is not correct. Please input right value!'
    return json.dumps({'msg':msg}),404,{'Content-Type':'application/json'}

@app.errorhandler(500)
def page_not_found(error):
    msg = 'Error! Please check again!'
    return json.dumps({'msg':msg}),500,{'Content-Type':'application/json'}

@app.errorhandler(502)
def page_not_found(error):
    msg = 'Bad Gateway!'
    return json.dumps({'msg':msg}),502,{'Content-Type':'application/json'}

if __name__ == '__main__':
    app.run(host='192.168.0.11',port=8000,debug=True)
