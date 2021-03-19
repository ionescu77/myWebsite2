import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/src')

INTERP = os.path.expanduser("/home/tu_ionescu77/bin/python")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'/home/tu_ionescu77/bin')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
