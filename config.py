import os
import random
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOSTNAME = os.uname()[1]
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    BG_COLOR = ','.join([str(element) for element in random.sample(range(255), 3)])
