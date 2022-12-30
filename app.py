from unittest import result
from flask import Flask, render_template, redirect, request, url_for
import Caption_it
from passlib.hash import md5_crypt as md5
from passlib.hash import sha256_crypt as sha256
from passlib.hash import sha512_crypt as sha512

app = Flask(__name__)


# @app.route('/main')
# def hello2():
#     return render_template("home.html")


@app.route('/',  methods=['GET'])
def hello():
    return render_template("index.html")


@app.route('/',  methods=['GET', 'POST'])
def caption():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)  # ./static/images.jpg
        f.save(path)
        caption = Caption_it.caption_this_image(path)
        # print(caption)
        result_dic = {
            'image': path,
            'caption': caption
        }
    return render_template("index.html", answer=result_dic)
    # return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
