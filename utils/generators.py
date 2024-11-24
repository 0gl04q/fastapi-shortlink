import random
from settings.config import settings
from pydantic import HttpUrl


def generate_slug():
    random.shuffle(settings.GENERATE_LIST)
    return ''.join(settings.GENERATE_LIST[:6])


def generate_url(slug):
    return HttpUrl(f'{settings.HTTP_SCHEME}://{settings.BASE_URL}/{slug}')
