import inspect
import logging
from functools import wraps


ENCODING = "utf-8"
trace_log = logging.getLogger("trace_log")

_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

fh = logging.FileHandler("log/trace.log", encoding=ENCODING)
fh.setLevel(logging.DEBUG)
fh.setFormatter(_format)
trace_log.addHandler(fh)
trace_log.setLevel(logging.DEBUG)


def log(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        stack = inspect.stack()
        trace_log.debug(
            f"Функция {fn.__name__} была вызвана из функции {stack[1].function}"
        )
        return fn(*args, **kwargs)
    return inner
