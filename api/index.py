from flask import Flask, render_template , request , redirect
from flask_cors import CORS 
from id_validator import validator
import requests
import json  # json解析用的
app = Flask(__name__)
cors = CORS(app)
def getBingImg():
    try:
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'user-agent': 'wuyuan.dev',
            # 不是必须
        }
 
        response = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN",
                                headers=headers,  # 请求头
                                timeout=3,  # 设置请求超时时间
                                )
        response = json.loads(response.text)  # 转化为json
        imgList = []
        for item in response['images']:
            imgList.append({
                'copyright': item['copyright'],  # 版权
                'date': item['enddate'][0:4] + '-' + item['enddate'][4:6] + '-' + item['enddate'][6:],  # 时间
                'urlbase': 'https://cn.bing.com' + item['urlbase'],  # 原始图片链接
                'url': 'https://cn.bing.com' + item['url'],  # 图片链接
            })
        return imgList[0] # 返回一个数据数组
    except:
        return False
 
 

@app.route('/bing/json')
def bingjson():
    return  json.loads(json.dumps(getBingImg(),ensure_ascii=False))
@app.route('/bing/img')
def bingimg():
    return redirect(json.loads(json.dumps(getBingImg(),ensure_ascii=False))['url'])
@app.route('/id/check')
def check():
    id=request.args['id']
    return str(validator.is_valid(id)) # 大陆居民身份证 18 位
@app.route('/id/info')
def info():
    id=request.args['id']
    return str(validator.get_info(id)) # 大陆居民身份证 18 位
@app.route('/id/generate')
def generate():
    area=request.args['area']
    birthday=request.args['birthday']
    sex=request.args['sex']
    return str(validator.fake_id(True, area, birthday, sex)) # 大陆居民身份证 18 位
@app.route('/id/to')
def to():
    id=request.args['id']
    return str(validator.upgrade_id(id)) # 大陆居民身份证 18 位

@app.route('/')
def result():
   return render_template('index.html')
#if __name__ == '__main__':
#   app.run(debug = True)