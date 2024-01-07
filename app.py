import os
import webbrowser
from lib.youtube_downloader import download_audio
from flask import Flask, render_template, redirect, request, url_for

class YoutubeAudioDownloaderGUI:
    """
    GUI web de l'application YoutubeAudioDownloader.
    """
    APP_URL = 'http://127.0.0.1:5000/'
    INDEX_PATH = 'index.html'
    URL_TAG = 'url'

    def __init__(self):
        """
        Initialise le GUI de l'application YoutubeAudioDownloader.
        PRE: -
        POST : Initialise l'interface GUI de l'application YoutubeAudioDownloader avec l'attribut suivant :
               - app : l'application web.
               Route l'application avec plusieurs fonctions.
               - '/' pour la fonction 'index'
               - '/download' pour la fonction 'download'
        """
        self.app = Flask(__name__, static_url_path='/static')

        self.app.route('/')(self.index)
        self.app.route('/download')(self.download)

    def index(self) -> str:
        """
        Fournit la page d'accueil de l'application YoutubeAudioDownloader.
        PRE : -
        POST : Retourne la page html 'index.html' d'accueil de l'application YoutubeAudioDownloader.
        """
        return render_template(self.INDEX_PATH)

    def download(self):
        """
        Télécharge la vidéo dont l'URL a été fournie par l'utilisateur dans le GUI de l'application.
        PRE : Le formulaire de téléchargement de la page d'accueil du GUI de l'application doit être disponible et
              complété.
        POST : Télécharge la vidéo dont l'URL a été fournie par l'utilisateur dans le GUI de l'application.
               Renvoie la page HTML d'accueil de l'application YoutubeAudioDownloader
        """
        url = request.form.get(self.URL_TAG)
        download_audio(url)
        return redirect('/')

    def open_browser(self):
        """
        Ouvre le navigateur par défaut de l'utilisateur sur la page de l'application Youtube Audio Downloader
        PRE : -
        POST : Ouvre le navigateur par défaut de l'utilisateur sur la page la première adresse locale.
               Si l'application est lancée, la page équivaut à celle de l'application Youtube Audio Downloader
        """
        webbrowser.open_new(self.APP_URL)

    def run(self, forced_window=False):
        """
        Lance le GUI de l'application YoutubeAudioDownloader.
        PRE: - forced_window : booléen
               Par défaut, faux
        POST: Lance le GUI web de l'application YoutubeAudioDownloader qur l'adresse locale.
              L'utilisateur pourra télécharger des vidéos Youtube via l'URL de celles-ci.
              Si l'option forced_window est activée, ouvre une page du navigateur sur l'application.
        """
        if forced_window:
            self.open_browser()

        self.app.run()


if __name__ == '__main__':
    app = YoutubeAudioDownloaderGUI()
    app.run(forced_window=False)
