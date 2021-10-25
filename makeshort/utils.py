import base64
import hashlib


def short_url_gen(url: str) -> str:
    myhash = hashlib.sha1(url.encode('utf-8'))
    result = base64.b64encode(myhash.digest())
    str_res = str(result[0:6]).replace('b', '').replace("'", '')
    return str_res


def create_url(obj, obj_url: str):
    new = short_url_gen(obj_url)
    # print(obj)  # https://m.facebook.com/anr.kotov.1?ref=bookmarks
    # print(obj.__class__)  # <class 'makeshort.models.ShortUrl'>
    # print(obj.__class__.__name__)  # ShortUrl
    obj_class = obj.__class__
    check_if_exists = obj_class.objects.filter(short_url=new).exists()
    if check_if_exists: 
        return create_url(obj_url) 
    else:
        return new
