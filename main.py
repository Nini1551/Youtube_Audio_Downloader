"""
YOUTUBE AUDIO DOWNLOADER
by HUYBRECHTS Louis

Télécharge l'audio d'une vidéo Youtube au format mp4.
L'utilisateur doit passer en paramètres certains arguments à l'appel du script :
- url : L'url de la vidéo Youtube à télécharger.
  Par défaut, une surprise vous attend.
- output : Le chemin du dossier où sera téléchargée la vidéo.
  Si le dossier n'existe pas, il est créé.
  Par défaut, le fichier sera téléchargé dans un dossier download_arguments situé dans le dossier courant.
- progress : Si la progression du téléchargement doit être affichée ou non.
  Par défaut, la progression ne sera pas affichée.
- -f (--file) : fichier texte composé d'urls de vidéo Youtube à télécharger séparées par des retours à la ligne.
  L'option n'est pas obligatoire.
"""
import os
from lib.args import get_args
from lib.youtube_downloader import download_audio, download_audios_from_file


if __name__ == '__main__':
    args = get_args()

    os.makedirs(args.output, exist_ok=True)

    if args.file is None:
        download_audio(args.url, args.output, args.progress)
    else:
        download_audios_from_file(args.file, args.output, args.progress)
