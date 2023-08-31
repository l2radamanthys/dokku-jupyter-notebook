# dokku-jupyter-notebook
Levantar jupyter notebook en instancia para un solo usuario.

# Librerias incluidas

- pandas
- numpy
- plotly
- dateutils
- tabulate
- requests
- beautifulsoup4
- scrapy
- lxml
- openpyxl

# Instalación

    dokku apps:create notebook
    dokku proxy:ports-add notebook http:8888:5000

Agregar repositorio

    git remote add dokku dokku@<yourserver>:notebook

Subir proyecto

    git push dokku main:master -f

# Set Password

Aquí deberemos generar una nueva contraseña, para ello lo mas fácil es abrir un notebook y generarla con el siguiente comando 

    from notebook.auth import passwd
    passwd()

Donde deberemos elegir la contraseña a generar, y nos generara un sha

    dokku config:set notebook NOTEBOOK_PASSWORD="<your-password>"

# Persist Notebooks


Crear el directorio dentro de `/var/lib/dokku/data/storage` con el nombre de la app

    sudo mkdir -p /var/lib/dokku/data/storage/notebooks

Vincular el directorio, necesitamos montar en disco un directorio donde almacenaremos los
notebooks que vayamos creando.

    dokku storage:mount notebook /var/lib/dokku/data/storage/notebooks:/notebooks

Notar que en esta caso montamos el storage como `/notebooks` deberemos configurar esta ruta como 
variable de entorno

    dokku config:set notebook NOTEBOOK_DIR="/notebooks"
