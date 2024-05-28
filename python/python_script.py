import os

## Carpeta dataset ##

location= 'C:/Users/Galgo.DESKTOP-NU9OB99/Documents/proyecto_parcial/python/dataset'

### Validar si existe carpeta ###
if not os.path.exists(location): ##carpeta no existe
    ##creo la carpeta
    os.mkdir(location)
else: ##carpeta existe
    ##borrar contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name)) ## eliminar los archivos
        for name in dirs:
            os.rmdir(os.path.join(root, name)) ## eliminar las carpetas

### Importar libreria API Kaggle ###

from kaggle.api.kaggle_api_extended import KaggleApi

### Autenticarnos ###

api = KaggleApi()
api.authenticate()

### Descargar dataset ###
# print(api.dataset_list(search='')) #listo los dataset disponibles


# api.dataset_download_file('rahulvyasm/netflix-movies-and-tv-shows', 'netflix_titles.csv', path=location, force=True, quiet=False)
api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location,force=True,quiet=False,unzip=True)

