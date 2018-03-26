import datetime
from celery.schedules import crontab


class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    RECAPTCHA_PUBLIC_KEY = "6LdKkQQTAAAAAEH0GFj7NLg5tGicaoOus7G9Q5Uw"
    RECAPTCHA_PRIVATE_KEY = '6LdKkQQTAAAAAMYroksPTJ7pWhobYb88fTAcxcYn'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://../database.db'
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
    # CELERY_BACKEND_URL = "amqp://guest:guest@localhost:5672//"
    CELERY_BACKEND_URL = "amqp://guest:guest@localhost:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"

    CACHE_TYPE = 'simple'

    CELERYBEAT_SCHEDULE = {
        # 'log-every-30-seconds': {
        #     'task': 'webapp.tasks.log',
        #     'schedule': datetime.timedelta(seconds=30),
        #     'args': ("Message",)
        # }
        'weekly-digest': {
            'task': 'task.digest',
            'schedule': crontab(day_of_week=6, hour='10')
        }
    }
