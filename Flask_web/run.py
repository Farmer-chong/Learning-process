# base.html->  {header}
# user.html-> {task} 题目
#             {dead_line} 截止日期
import os
from flask import Flask
from flask import render_template
from flask import request
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
#  题目 & 截止日期
contents = [
    {'task':'写一篇关于这学期C语言学习的笔记（建议使用markdown来写）',
    'dead_line':'一月五号前'},
    {'task':'学习HTML+CSS，并利用所学知识写一个网页。题材不限。',
    'dead_line':'10天时间'},
    {'task':'Linux命令行',
    'dead_line':'2天内完成'},
    {'task':'vscode课后作业',
    'dead_line':'2天内完成'},
    {'task':'把自己写的网页部署到服务器上',
    'dead_line':'2天内完成'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    header = "科技部肥宅快乐大礼包"
    return render_template('user.html',header = header,contents=contents)

@app.route('/upload', methods=['post'])
def upload():
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
    return '<h1>file upload successfully</h1>'

if __name__ == "__main__":
    print(app.root_path)
    print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    app.run(host="0.0.0.0",port=5000)