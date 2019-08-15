from flask import Flask,sessions
from flask import request

app = Flask(__name__)
app.secret_key = 'liuyang'
print(request)
@app.route("/")
def index():
    #执行session 对象的__setitem__方法
    #在空字典中写值
    #在空字典中获取值
    sessions['xxx'] = 123
    return "index 页面"





if __name__ == "__main__":
    #一旦请求进来就会执行call 方法
    app.run()
    app.__call__()