# Configuration file for jupyter-notebook.
import os
import uuid
import IPython.lib


c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True
c.NotebookApp.token = ''
c.NotebookApp.password = os.getenv('NOTEBOOK_PASSWORD', '')
c.NotebookApp.notebook_dir = os.getenv('NOTEBOOK_DIR', '/notebooks')
