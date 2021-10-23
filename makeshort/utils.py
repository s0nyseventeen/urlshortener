import string
from random import choice

symbols = "".join([string.ascii_lowercase, string.ascii_uppercase,
                   string.digits])


def short_url_gen(length=6, ascii_letters=symbols) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))  # _ because we don't need it the future


def create_url(obj, length=6):
    new = short_url_gen(length=length)
    #print(obj)  # https://m.facebook.com/anr.kotov.1?ref=bookmarks
    #print(obj.__class__)  # <class 'makeshort.models.ShortUrl'>
    #print(obj.__class__.__name__)  # ShortUrl
    obj_class = obj.__class__
    check_ifexists = obj_class.objects.filter(short_url=new).exists()
    return create_url(length=length) if check_ifexists else new
