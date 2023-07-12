#+++++++++++ DJANGO +++++++++++
#To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/laserparams/mysite/mysite/settings.py'
# and your manage.py is is at '/home/laserparams/mysite/manage.py'
path = '/home/laserparams/laser_db'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'laser_db.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

