from configs.default import RESPONSE, ALERT, ERROR

# Ответы сервера
RESPONSE_200 = {
    RESPONSE: 200,
    ALERT: None

}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}

RESPONSE_402 = {
    RESPONSE: 402,
    ERROR: "Hеправильный пароль или нет учетной записи с таким именем"
}

RESPONSE_409 = {
    RESPONSE: 409,
    ERROR: "Такое имя пользователя уже существует"
}