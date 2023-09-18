import os

if os.getenv('ENV') == 'PRODUCTION':
    from .production import *
else:
    from .develop import *
