import os
import webbrowser
from lib.youtube_downloader import download_audio
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    download_audio(url)
    return redirect('/')

def open_browser():
    """
    Ouvre le navigateur par défaut de l'utilisateur sur la page de l'application Youtube Audio Downloader
    PRE : -
    POST : Ouvre le navigateur par défaut de l'utilisateur sur la page la première adresse locale.
           Si l'application est lancée, la page équivaut à celle de l'application Youtube Audio Downloader
    """
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    app.run()
