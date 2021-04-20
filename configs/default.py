import logging

# Порт по умолчанию
DEFAULT_PORT = 5555
# IP адрес по умолчанию
DEFAULT_IP_ADDRESS = "127.0.0.1"
# Максимальная очередь подключений
MAX_CONNECTIONS = 0
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка
ENCODING = "utf-8"
# Уровень логирования
LOGGING_LEVEL = logging.DEBUG

# Основные ключи:
ACTION = "action"
TIME = "time"
USER = "user"
ACCOUNT_NAME = "account_name"
SENDER = "from"
DESTINATION = "to"

TYPE = "type"
STATUS = "status"
ACCOUNT_PASSWORD = "account_password"
PRESENCE = "presence"
MESSAGE = "message"
MESSAGE_TEXT = "message_text"
QUIT = "quit"
RESPONSE = "response"
ERROR = "error"
ALERT = "alert"

