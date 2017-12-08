import dotenv

dotenv.load()

if dotenv.get('HEROKU'):
    from .production import *
else:
    from .development import *