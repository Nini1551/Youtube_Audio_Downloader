"""
YOUTUBE AUDIO DOWNLOADER
by HUYBRECHTS Louis
23/12/2023

Télécharge l'audio d'une vidéo Youtube au format mp4.
L'utilisateur doit passer en paramètres certains arguments à l'appel du script :
- url : L'url de la vidéo Youtube à télécharger.
- output : Le chemin du dossier où sera téléchargée la vidéo.
  Si le dossier n'existe pas, il est créé.
  Par défaut, le fichier sera téléchargé dans un dossier download_arguments situé dans le dossier courant.
- progress : Si la progression du téléchargement doit être affichée ou non.
  Par défaut, la progression ne sera pas affichée.
"""
import os
import argparse
from pytube import YouTube


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
          - output_path: chemin du dossier dans lequel le fichier mp4 sera téléchargée
            Par défaut, les fichiers seront téléchargées dans le dossier courant.
          - display_progress: un booléen
            Par défaut, faux
    POST : Télécharge l'audio d'une vidéo Youtube au format mp4 via son url.
           Le fichier sera téléchargé dans le dossier précisé par l'utilisateur.
           Précise le début et la fin du téléchargement en plus du nom de la vidéo téléchargée.
           Si l'option est sélectionnée, affiche la progression du téléchargement.
    """
    on_progress_callback = on_progress if display_progress else None

    yt = YouTube(url, on_progress_callback=on_progress_callback)
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Téléchargement de la vidéo : \"{yt.title}\"")
    audio.download(output_path)
    print("Téléchargement terminé.")

def get_args() -> argparse.Namespace:
    """
    Crée et fournit un utilitaire des arguments du script lancé
    PRE : Les arguments suivants doivent être précisés au lancement du script.
            - L'url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
            - -o (--output) : chemin du dossier dans lequel le fichier mp4 sera téléchargée
              Par défaut, les fichiers seront téléchargées dans le dossier courant.
            - --progress : stocke vrai
    POST : Renvoie l'utilitaire des arguments du cript lancé aux propriétés suivantes:
           - url (str) : url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
           - output_path (str) : chemin du dossier dans lequel le fichier mp4 sera téléchargée
           - progress (bool) : si la progression du téléchargement doit être affichée ou non
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
    parser.add_argument(
        '--progress',
        action='store_true',
        help="Si la progression du téléchargement doit être affichée ou non"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    os.makedirs(args.output, exist_ok=True)

    download_audio(args.url, args.output, args.progress)
