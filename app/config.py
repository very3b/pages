import os

class Config(object):
    SECRETE_KEY=os.environ.get('SECRETE_KEY') or 'aaadsfa'
