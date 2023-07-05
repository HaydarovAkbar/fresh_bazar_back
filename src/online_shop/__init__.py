from .base import *
from decouple import config

env = config('ENV_NAME')
if env == 'production':
    from .production import *
elif env == 'localhost':
    from .local import *
elif env == 'staging':
    from .staging import *
else:
    print('No environment chosen!')