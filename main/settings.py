# Settings loader file.

import os
import glob
import re
import socket

pwd = os.path.dirname(__file__)

# load in the individual files
configuration_files = glob.glob(os.path.join(pwd, 'settings', '*.django-settings'))

# order them by the number (10-, 20-)
configuration_files.sort()

# Open and compile each file
for f in configuration_files:
    exec(compile(open(os.path.abspath(f)).read(), f, 'exec'), globals(), locals())

machine_name = re.sub('[^A-z0-9._]', '_', socket.gethostname())
machine_settings = os.path.join(pwd,'settings/%s.py'%machine_name)

try:
    f = machine_settings
    exec(compile(open(os.path.abspath(f)).read(), f, 'exec'), globals(), locals())
except IOError:
    print "No machine settings found. We looked here: %s"%machine_settings
