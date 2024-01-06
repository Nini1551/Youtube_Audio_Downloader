import os
from lib.youtube_downloader import download_audio
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    download_audio(url, './downloaded_audios')
    return redirect('/')


if __name__ == '__main__':
    app.run()
