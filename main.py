
# main.py

from flask import Flask, render_template, request, redirect, url_for
import difflib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files['file1']
    file2 = request.files['file2']
    text1 = file1.read().decode('utf-8')
    text2 = file2.read().decode('utf-8')
    diff = difflib.HtmlDiff().make_table(text1.splitlines(), text2.splitlines())
    return render_template('compare.html', diff=diff)

if __name__ == '__main__':
    app.run(debug=True)
