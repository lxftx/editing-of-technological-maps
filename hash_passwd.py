import hashlib


def hash_password(password):
        # Создаем объект хэш-функции
    hash_object = hashlib.sha256()

        # Преобразуем пароль в байтовую строку перед хэшированием
    password = password.encode('utf-8')

        # Обновляем хэш с использованием пароля
    hash_object.update(password)

        # Получаем зашифрованный пароль (хэш)
    hashed_password = hash_object.hexdigest()

    return hashed_password

def check_password(input_password, stored_hashed_password):
    input_password = input_password.encode('utf-8')  # Преобразуем введенный пароль в байты
    input_hash = hashlib.sha256(input_password).hexdigest()  # Хэшируем введенный пароль

    return input_hash == stored_hashed_password  # Сравниваем хэши