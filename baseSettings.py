import os
import sys

APP_NAME = 'ACG Thread Manager'
APP_VERSION = '1.0.0'

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(__file__)