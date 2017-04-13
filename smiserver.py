import os
import sys
from flask import Flask, request, redirect, url_for, flash, render_template, Response
from werkzeug.utils import secure_filename
from script2sami import mkSami


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/smiserver'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'smiserver'


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
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        try:
            sami = mkSami(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        except Exception as e:
            flash('오류: 자막 생성 실패 \n'+e.message)
            return redirect(request.url)
        
        return Response(sami, mimetype="application/smil", 
                        headers={"Content-Disposition":"attachment;filename=subtitle.smi"})
    return greating()

#    result = mkSami(os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                    "script_sample.xml"))
#    return result
