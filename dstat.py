from flask import Flask, render_template
import os
os.system("pip install Flask")
os.system("pip2 install Flask")
os.system("pip3 install Flask")
app = Flask(__name__)
num = 0

@app.route('/')
def index():
    global num
    num = num + 1
    return str(num)

if __name__ == '__main__':
    app.run(host='128.116.123.3', host=80)
