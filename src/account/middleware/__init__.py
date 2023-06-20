try:
    from .middlewares import SqlInectionMiddleware
except ImportError:
    pass