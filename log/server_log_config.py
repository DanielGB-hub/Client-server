import logging.handlers
import sys

ENCODING = "utf-8"

server_log = logging.getLogger("server_log")

_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

fh = logging.handlers.TimedRotatingFileHandler(filename="log/server.log", interval=1, encoding=ENCODING,
                                               when="midnight", backupCount=10)
fh.setLevel(logging.DEBUG)
fh.setFormatter(_format)

crit_handler = logging.StreamHandler(sys.stderr)
crit_handler.setLevel(logging.CRITICAL)
crit_handler.setFormatter(_format)

server_log.addHandler(fh)
server_log.addHandler(crit_handler)
server_log.setLevel(logging.DEBUG)
