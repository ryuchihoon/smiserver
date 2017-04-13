import os
import sys
from flask import Flask
from script2sami import mkSami


app = Flask(__name__)


@app.route('/')
def hello_world():
    result = mkSami(os.path.join(os.path.dirname(os.path.abspath(__file__)), "script_sample.xml"))
    return result
