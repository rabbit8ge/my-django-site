This is heyiping's personal website created at 9/9/2015.
Demo site:http://kdjohar.in/

django-wpadmin
django-ckeditor
django-tagging
django-pipeline
django-htmlmin
python-memcached (not install, comment out CACHE in settings.py)

How to run:
 . Install python 2.7.
 . Install sae package: pip install sae-python-dev. See http://www.sinacloud.com/doc/sae/python/tools.html
 . New a .pth file in <python_dir>/lib/site-packages/, the content is the folder of <current_directory>/site-packages
 . Run SAE as a simulation platform: dev_server.py in current folder.
 . Open http://localhost:8080/ to see the website.
 
Set myblog.settings.DEBUG = True if there's any error to debug.

The administration panel is: <host>/hypadmin

User and passwords for both local and SAE administration.
admin user: he
admin password: headminheadmin

Development:
The branch 1 is for releasing and branch 3 is for development.