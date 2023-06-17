from decouple import config
from .base import *

env_type = config('ENV_NAME')
if env_type == 'production':
    from .production import *
elif env_type == 'localhost':
    from .local import *
elif env_type == 'staging':
    from .staging import *
else:
    print('No environment chosen!')
