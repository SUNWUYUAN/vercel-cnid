from flask import Flask, render_template , request
from flask_cors import CORS 
from id_validator import validator
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return 'Hello, world'

@app.route('/check')
def check():
    id=request.args['id']
    return str(validator.is_valid(id)) # 大陆居民身份证 18 位
@app.route('/info')
def info():
    id=request.args['id']
    return str(validator.get_info(id)) # 大陆居民身份证 18 位
@app.route('/generate')
def generate():
    area=request.args['area']
    birthday=request.args['birthday']
    sex=request.args['sex']
    return str(validator.fake_id(True, area, birthday, sex)) # 大陆居民身份证 18 位
@app.route('/to')
def to():
    id=request.args['id']
    return str(validator.upgrade_id(id)) # 大陆居民身份证 18 位

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
#if __name__ == '__main__':
#   app.run(debug = True)