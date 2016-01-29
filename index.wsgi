import sae
import os
import sys

# insert before importing wsgi.
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))
sys.path.insert(0, os.path.join(root, 'site-packages'))
print 'sys.path: ', sys.path

import django
print 'django version: ', django.VERSION

from myblog import wsgi

application = sae.create_wsgi_app(wsgi.application)