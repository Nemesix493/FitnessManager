import os

if os.getenv('ENV') == 'PRODUCTION':
    from .production import *  # noqa: F401
else:
    from .develop import *  # noqa: F401
