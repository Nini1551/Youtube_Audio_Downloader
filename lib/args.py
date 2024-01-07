"""
Définition du parser du projet Youtube Audio Downloader
"""
import argparse
from lib.youtube_downloader import get_downloads_folder

def get_args() -> argparse.Namespace:
    """
    Crée et fournit un utilitaire des arguments du script lancé
    PRE : Les arguments suivants doivent être précisés au lancement du script.
            - L'url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
              Par défaut, une chaîne vide (surprise ...)
            - -o (--output) : chemin du dossier dans lequel le fichier mp4 sera téléchargée
              Par défaut, les fichiers seront téléchargées dans le dossier Téléchargements de l'utilisateur.
            - --progress : stocke vrai
            - -f (--file) : nom d'un fichier texte ou None (pas obligatoire).
              Le fichier texte est composé d'urls de vidéos Youtube séparées par un retour à la ligne.
              Par défaut, None
            - --gui : stocke vrai
    POST : Renvoie l'utilitaire des arguments du cript lancé aux propriétés suivantes:
           - url (str) : url d'une vidéo Youtube publique et non-limitée aux utilisateurs majeurs
           - output_path (str) : chemin du dossier dans lequel le fichier mp4 sera téléchargée
           - progress (bool) : si la progression du téléchargement doit être affichée ou non
           - file (str) : fichier texte composé d'urls de vidéo Youtube à télécharger séparées par des retours à la ligne
           - gui (bool) : si l'utilisateur veut ouvrir le GUI de l'application.
    """
    parser = argparse.ArgumentParser(description="Télécharge l'audio d'une vidéo YouTube au format audio mp4.")
    parser.add_argument(
        'url',
        type=str, default='', nargs='?',
        help="URL de la vidéo YouTube"
    )
    parser.add_argument(
        '-o', '--output',
        type=str, default=get_downloads_folder(),
        help="Chemin de sortie (par défaut: dossier courant)"
    )
    parser.add_argument(
        '-f', '--file',
        type=str, default=None,
        help="Fichier texte composé d'URLs de vidéo Youtube à télécharger séparées par des retours à la ligne"
    )
    parser.add_argument(
        '--progress',
        action='store_true',
        help="Si la progression du téléchargement doit être affichée ou non"
    )
    parser.add_argument(
        '--gui',
        action='store_true',
        help="Ouvre le GUI de l'application"
    )
    return parser.parse_args()
