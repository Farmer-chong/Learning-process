# base.html->  {header}
# user.html-> {task} 题目
#             {dead_line} 截止日期
import time
import os
from flask import Flask, make_response
from flask import render_template
from flask import request
from werkzeug import secure_filename
app = Flask(__name__)
# header
header = "科技部肥宅快乐大礼包"
#  题目 & 截止日期
contents = [
    {'task': '签到->上传一个txt文档，用自己的名字命名。',
    'dead_line': '∞'},
    {'task':'写一篇关于这学期C语言学习的笔记（建议使用markdown来写）',
    'dead_line':'两天'},
    # {'task':'学习HTML+CSS，并利用所学知识写一个网页。题材不限。',
    # 'dead_line':'10天'},
    # {'task':'Linux命令行',
    # 'dead_line':'2天内完成'},
    # {'task':'vscode课后作业',
    # 'dead_line':'2天内完成'},
    # {'task':'把自己写的网页部署到服务器上',
    # 'dead_line':'2天内完成'}
]

# 红包口令


@app.route('/', methods=['GET', 'POST'])
def index():
    headers = request.headers
    print(headers)
    print(type(headers))
    print(type(request.headers))
    resp = make_response(render_template('user.html',header = header,contents=contents))  # 响应体数据
    #resp.status = "999 itcast"  # 状态码
    resp.headers["lucky-Money-Key"] = "2333333"
    return resp  # 通过字典的形式添加响应头 

@app.route('/upload', methods=['post'])
def upload():
    f = request.files['file']
    FileName = request.form['task']
    Time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    FilePaht = os.getcwd() + '/uploads/' + FileName # Linux下用/ Windows用 \
    print(FilePaht)
    print(Time)
    if os.path.exists(FilePaht) is False:
        os.mkdir(FilePaht)
    app.config['UPLOAD_PATH'] = os.path.join(FilePaht)
    f.save(os.path.join(app.config['UPLOAD_PATH'], Time + '_' + f.filename))
    return '<h1>file upload successfully</h1>'

@app.route('/admin')
def admin():
    return render_template('admin.html',header=header)

@app.route('/update', methods=['post'])
def update():
    task = request.form['task']
    dead_line = request.form['dead_line'] 
    contents = request.form
    print(contents[1])
    print(task, dead_line)
    return '<h1> update successful </h1>'

if __name__ == "__main__":
    print(app.root_path)
    print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    print(type(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))))
    app.run(host="0.0.0.0",port=5000)
    