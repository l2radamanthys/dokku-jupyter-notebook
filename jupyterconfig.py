import os
import uuid
import IPython.lib

c = get_config()
password = os.getenv('JUPYTER_NOTEBOOK_PASSWORD', default=str(uuid.uuid4()))
c.NotebookApp.password = IPython.lib.passwd(password)
