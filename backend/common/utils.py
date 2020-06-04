import inspect
import time
import string

from flask import jsonify
from zhon.hanzi import punctuation


def get_classes(arg):
    classes = []
    clsmembers = inspect.getmembers(arg, inspect.isclass)
    for (name, _) in clsmembers:
        classes.append(name)
    return classes


def field_struct_decorator(code=0, errmsg="", **args):
    unix_time = int(time.time())
    back_jsonify = {'code': code,
                    "data": {k: v for k, v in args.items()},
                    'unixTime': unix_time,
                    "errMsg": errmsg}
    return jsonify(back_jsonify)


remap = {ord('\t'): " ",
         ord('\f'): " ",
         ord('\r'): None,
         ord('\n'): None
         }

chrs = dict.fromkeys(ord(c) for c in string.punctuation)
chrs.update(dict.fromkeys(ord(c) for c in punctuation))
chrs.update(remap)
