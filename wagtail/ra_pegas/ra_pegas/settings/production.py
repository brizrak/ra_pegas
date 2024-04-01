from .base import *
from decouple import config

DEBUG = config('DEBUG')

try:
    from .local import *
except ImportError:
    pass
