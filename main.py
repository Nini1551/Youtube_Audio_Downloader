"""
YOUTUBE AUDIO DOWNLOADER
by HUYBRECHTS Louis
22/12/2023

Télécharge l'audio d'une vidéo Youtube au format mp4.
L'utilisateur doit préciser dans les variables suivantes :
- YOUTUBE_URL : L'url de la vidéo Youtube à télécharger.
- OUTPUT_PATH : le chemin du dossier où sera téléchargée la vidéo.
  Si le dossier n'existe pas, il est créé.
"""
import os
from pytube import YouTube


YOUTUBE_URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
OUTPUT_PATH = './download_audios'

def download_audio(url: str, output_path: str = '.'):
    """
    Télécharge l'audio d'une vidéo Youtube au format mp4
    PRE : - url: url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
          - output_path: chemin du dossier dans lequel le fichier mp4 sera téléchargée
            Par défaut, les fichiers seront téléchargées dans le dossier courant.
    POST : Télécharge l'audio d'une vidéo Youtube au format mp4 via son url.
           Le fichier sera téléchargé dans le dossier précisé par l'utilisateur.
           Précise le début et la fin du téléchargement en plus du nom de la vidéo téléchargée.
    """
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Téléchargement de la vidéo : \"{yt.title}\"")
    audio_stream.download(output_path)
    print("Téléchargement terminé.")


if __name__ == '__main__':
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    download_audio(YOUTUBE_URL, OUTPUT_PATH)
