"""
YOUTUBE AUDIO DOWNLOADER
by HUYBRECHTS Louis
22/12/2023

Télécharge l'audio d'une vidéo Youtube au format mp4.
L'utilisateur doit passer en paramètres certains arguments à l'appel du script :
- url : L'url de la vidéo Youtube à télécharger.
- output : Le chemin du dossier où sera téléchargée la vidéo.
  Si le dossier n'existe pas, il est créé.
  Par défaut, le fichier sera téléchargé dans un dossier download_arguments situé dans le dossier courant.
"""
import os
import argparse
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

def get_args() -> argparse.Namespace:
    """
    Crée et fournit un utilitaire des arguments du script lancé
    PRE : Les arguments suivants doivent être précisés au lancement du script.
            - L'url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
            - -o (--output) : chemin du dossier dans lequel le fichier mp4 sera téléchargée
              Par défaut, les fichiers seront téléchargées dans le dossier courant.
    POST : Renvoie l'utilitaire des arguments du cript lancé aux propriétés suivantes:
           - url (str): url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
           - output_path (str): chemin du dossier dans lequel le fichier mp4 sera téléchargée
    """
    parser = argparse.ArgumentParser(description="Télécharge l'audio d'une vidéo YouTube au format audio mp4.")
    parser.add_argument(
        'url',
        type=str,
        help="URL de la vidéo YouTube"
    )
    parser.add_argument(
        '-o', '--output',
        type=str, default='./download_audios',
        help="Chemin de sortie (par défaut: dossier courant)"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    os.makedirs(args.output, exist_ok=True)

    download_audio(args.url, args.output)
