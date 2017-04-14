import os
import sys
from flask import Flask, request, redirect, url_for, flash, render_template, Response
from script2sami import mkSami


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.secret_key = 'smiserver_secret'


@app.route('/', methods=['GET'])
def greating():
    return render_template("index.html")

ALLOWED_EXTENSIONS = set(['txt', 'xml'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('오류: 파일 파트가 없음')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('오류: 파일을 선택하세요')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        try:
            sami = mkSami(file)
        except Exception as e:
            flash('오류: 자막 생성 실패 \n'+str(e))
            return redirect(request.url)
        
        return Response(sami, mimetype="application/smil", 
                        headers={"Content-Disposition":"attachment;filename=subtitle.smi"})
    return greating()
