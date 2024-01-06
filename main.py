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
import time
from pytube import YouTube
from lib.args import get_args


def on_progress(stream, chunk, bytes_remaining: int):
    """
    Affiche la progression actuelle du téléchargement.
    (Fonction callback utilitaire)
    PRE : - stream : flux actuellement téléchargé
          - chunk : bloc de données actuellement téléchargé
            Inutilisé, mais nécessaire à la fonction callback
          - bytes_remaining : nombre d'octets restant au téléchargement.
    POST : Après le téléchargement d'un bloc de données, affiche la progression du téléchargement du flux en entier.
    """
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentage = (bytes_downloaded / total_bytes) * 100
    print(f"Téléchargement en cours... {percentage:.2f}%")

def download_audio(url: str, output_path: str = '.', display_progress: bool = False):
    """
    Télécharge l'audio d'une vidéo Youtube au format mp4
    PRE : - url: url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
          - output_path: chemin du dossier dans lequel le fichier mp4 sera téléchargé
            Par défaut, le fichier sera téléchargé dans le dossier courant.
          - display_progress: un booléen
            Par défaut, faux
    POST : Télécharge l'audio d'une vidéo Youtube au format mp4 via son url.
           Le fichier sera téléchargé dans le dossier précisé par l'utilisateur.
           Précise le début et la fin du téléchargement en plus du nom de la vidéo téléchargée.
           Si l'option est sélectionnée, affiche la progression du téléchargement.
           Si l'url est une chaîne vide, une surprise vous attend.
    """
    if url == '':
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

    on_progress_callback = on_progress if display_progress else None

    yt = YouTube(url, on_progress_callback=on_progress_callback)
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Téléchargement de la vidéo : \"{yt.title}\"")
    audio.download(output_path)
    print("Téléchargement terminé.\n")

def download_audios_from_file(filename: str, output_path: str = '.', display_progress: bool = False):
    """
    Télécharge l'audio de plusieurs vidéos Youtube au format mp4.
    PRE : - filename : nom d'un fichier texte composé d'urls de vidéos Youtube séparées par un retour à la ligne
          - output_path: chemin du dossier dans lequel les fichiers mp4 seront téléchargés
            Par défaut, les fichiers seront téléchargés dans le dossier courant.
          - display_progress: un booléen
            Par défaut, faux
    POST : Télécharge l'audio de plusieurs vidéos Youtube au format mp4 via le nom du fichier texte.
           Les fichiers seront téléchargés dans le dossier précisé par l'utilisateur.
           Précise le début et la fin du téléchargement en plus du nom de la vidéo téléchargée.
           Entre chaque téléchargement, un temps d'attente est posé.
           Ignore les lignes vides.
           Si l'option est sélectionnée, affiche la progression du téléchargement.
    """
    sleep_time = 1
    with open(filename, 'r') as file:
        for url in file:
            url = url.strip()
            if url != '':
                download_audio(url, output_path, display_progress)
                time.sleep(sleep_time)


if __name__ == '__main__':
    args = get_args()

    os.makedirs(args.output, exist_ok=True)

    if args.file is None:
        download_audio(args.url, args.output, args.progress)
    else:
        download_audios_from_file(args.file, args.output, args.progress)
