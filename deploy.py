from flask import Flask,render_template, request, redirect,send_file,url_for
from pytubef import *
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        bro=request.form.get("link")
        bruh=request.form.get("type")
        k=foobart(bro,bruh)
        return send_file('test.'+k)
    return render_template('index.html')

if (__name__ == "__main__"):
    app.run(debug=True)
