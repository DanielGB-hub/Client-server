import logging.handlers
import sys

ENCODING = "utf-8"

client_log = logging.getLogger("client_log")

_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

fh = logging.FileHandler("log/client.log", encoding=ENCODING)
fh.setLevel(logging.DEBUG)
fh.setFormatter(_format)

crit_handler = logging.StreamHandler(sys.stderr)
crit_handler.setLevel(logging.CRITICAL)
crit_handler.setFormatter(_format)

client_log.addHandler(fh)
client_log.addHandler(crit_handler)
client_log.setLevel(logging.DEBUG)
