# Youtube Audio Downloader
by HUYBRECHTS Louis  
22/12/2023  

## Mode d'emploi
Télécharge l'audio d'une vidéo Youtube au format mp4.
L'utilisateur doit passer en paramètres certains arguments à l'appel du script :
- **url** : L'url de la vidéo Youtube à télécharger.
  Par défaut, une surprise vous attend.
- **output** : Le chemin du dossier où sera téléchargée la vidéo.
  Si le dossier n'existe pas, il est créé.
  Par défaut, le fichier sera téléchargé dans un dossier download_arguments situé dans le dossier courant.
- **progress** : Si la progression du téléchargement doit être affichée ou non.
  Par défaut, la progression ne sera pas affichée.
- **file** : fichier texte composé d'urls de vidéo Youtube à télécharger séparées par des retours à la ligne.
  L'option n'est pas obligatoire.
