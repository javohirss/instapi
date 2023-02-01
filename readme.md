# Получение данных с инстаграма через API.
Первым делом потребуется создать приложение с тестовыми пользователями. Инструкция [тут](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started) (шаги 1-3).

Для работы приложения на локальном сервере, нужно сменить протокол на https и указать локальный сервер как redirect_uri вашего приложения __Instagram Basic Display API__. Инструкция по смене протокола [тут](https://medium.com/@millienakiganda/creating-an-ssl-certificate-for-localhost-in-django-framework-45290d905b88)

Данные приложения, такие как client_id, client_secret нужно вставить в словарь
```
params = {
    'client_id' : ...,
    'client_secret' : ...,
    ,,,
}
```
файла views.py.
