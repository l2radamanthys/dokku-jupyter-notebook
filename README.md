# dokku-jupyter-notebook
Jupyter notebook and more for dokku

# Instalación

    dokku apps:create notebook
    dokku proxy:ports-add notebook http:8888:5000

Agregar repositorio

    git remote add dokku dokku@<yourserver>:notebook

Subir proyecto

    git push dokku main:master -f

# Set Password

dokku config:set notebook NOTEBOOK_PASSWORD="yourpassword"

# Persist Notebooks