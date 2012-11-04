"""
      $ ipcluster start -n 4
"""
from IPython.parallel import Client

c = Client()

print c.ids
c[:].apply_sync(lambda : "Hello, World")
