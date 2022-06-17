# Тестовое задание на должность Python Junior backend developer
## Описание: Тестовое задание состоит из трех частей. Реализация серверного приложения и REST API к нему, создание документации API и подготовка к развертыванию (опционально).
## Рекомендованный стек технологий:
```
Фреймворк для создания веб-приложений: fastapi, flask или прочие...
База данных: SQLite.
ORM или RAW: SQLAlchemy или прочие.
```
ВАЖНО! Проект должен быть создан в git-репозитории и открыт для просмотра. В самом проекте должен находится файл `requirements.txt`, где перечислены все использованные пакеты.
____

## Задание 1. Сервер:
Необходимо реализовать приложение, которое позволит получить «секретные» данные, расшифровать их, сохранить в БД и отправить обратно на сервер уже расшифрованные.
### Сам API представляет собой 3 метода. (запроса) названия оставляю за вами:

### Функционал `первого` метода представляет собой следующее (для вызова стоит использовать GET запрос):
1. Скачивает зашифрованные данные с удаленного сервера оп ссылке `GET` http://yarlikvid.ru:9999/api/top-secret-data.

   Если все сделано правильно, то данные прийдут в виде `json` строки, после чего эту строку стоит `десереализовать` в уже такой знакомый тип `list`.

2. Сохраняет все строки в базу данных! Структура таблицы очень проста...

   | id        | encrypted_text       | decrypted_text        | created_at                      |
       |-----------|----------------------|-----------------------|---------------------------------|
   | id записи | Зашифрованная строка | Расшифрованная строка | Временная метка создания записи |

3. Возвращает в ответе 201 `http-код` и список зашифрованных строк.

   Пример:
    ``` JSON
    [
        "xLTFq8ST1IvFpsWpxJXEl9SLxJTFq8SbxJHFqcSTxazElsSVxarFqcWn1IvEmcSbxJ3ElsSexJ7Ui8SaxJ7EnMWoxJTFq8SexazElsSVxarFqcST1IU=",
        "xLXFo8STxJrEkcST1IvElsSTxJHElcSYxJ/Em9SLxJbEntSLxJ/ElcSQxJ3ElsWg1IvEnMSbxJfEm8SQxazEk8SZxJvFqcWnxarFpNSF",
        "xL7FqsSQxJPUi8SVxJbEk9SLxJbEntSLxJzEm8SXxJvEkMWsxJPEmcSbxaXFqcWqxaTUi8WkxJnElsSV1IU="
    ]
    ```

### Функционал `второго` метода делает следующее (для вызова стоит использовать POST запрос):

ВАЖНО! Все остальные методы должны быть авторизованы. Для доступа используется простая `Basic` авторизация `(1)`

    ```
    username: qummy
    password: GiVEmYsecReT!
    ```

1. Выгружает из `БД` зашифрованные строки, без индексов и временных меток `list[str]`.

2. Делает `POST` запрос на удаленный сервер по адресу http://yarlikvid.ru:9999/api/decrypt

   Для выполнения необходимо добавить тело запроса (JSON), куда нужно будет передать список зашифрованных строк, полученных из первого метода:
    ```JSON
    [
        "xLTFq8ST1IvFpsWpxJXEl9SLxJTFq8SbxJHFqcSTxazElsSVxarFqcWn1IvEmcSbxJ3ElsSexJ7Ui8SaxJ7EnMWoxJTFq8SexazElsSVxarFqcST1IU=",
        "xLXFo8STxJrEkcST1IvElsSTxJHElcSYxJ/Em9SLxJbEntSLxJ/ElcSQxJ3ElsWg1IvEnMSbxJfEm8SQxazEk8SZxJvFqcWnxarFpNSF",
        "xL7FqsSQxJPUi8SVxJbEk9SLxJbEntSLxJzEm8SXxJvEkMWsxJPEmcSbxaXFqcWqxaTUi8WkxJnElsSV1IU="
    ]
    ```
3. В ответе придет такой же список, но уже расшифрованных строк в том же порядке. Эти строки необходимо сохранить в ту же БД.

   Каждая расшифрованная строка должна соответствовать зашифрованной!

4. Возвращает в ответе 201 `http-код` и список расшифрованных строк:

   Пример:
    ``` JSON
    [
        "Расшифрованная строка 1",
        "Расшифрованная строка 2",
        "Расшифрованная строка 3"
    ]
    ```

### Функционал `третьего` метода делает следующее (для вызова стоит использовать POST запрос):
1. Передача в метод ВАШЕГО имени и фамилии, а так же ссылки на репозиторий вашего выполненного проекта.

2. Подгрузить зашифрованные данные из БД и отправить на удаленный сервер `POST` http://yarlikvid.ru:9999/api/result

   Для выполнения необходимо добавить тело запроса (JSON):
    ```JSON 
    {
    "name": "Иван Иванов",
    "repo_url": "https://github.com/test/test-repo",
    "result": [
        "Расшифрованная строка 1",
        "Расшифрованная строка 2"
        ]
    }
    ```
- где `name` - это имя и фамилия отправителя; `repo_url` - ссылка на репозиторий с проектом (github, gitlab и т.д.); `result` - массив расшифрованных данных.
#### `Огромная просьба отправлять результат только один раз!`
#### Полная openapi документация по удаленному серверу представлена по ссылке http://yarlikvid.ru:9999/openapi.json
____
## Задание 2. Документация:
Документация это не самая любимая часть процесса разработки ПО, но когда приходиться связать нескольких разработчиков, то нужно помочь им понять друг друга.
Необходимо описать все методы API, а так же объекты передаваемые в тело запроса.
Для выполнения задания необходимо предоставить документацию в формате `OpenAPI specification` `(2)`.
Пример документации для расшифровки данных.
``` JSON
{
    "openapi": "3.0.2",
    "info": {
        "title": "TITLE",
        "version": "0.1.0"
    },
    "paths": {
        "/api/decrypt": {
            "post": {
                "summary": "Decrypt Top Secret Data",
                "operationId": "decrypt_top_secret_data_api_decrypt_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "Message",
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Decrypt Top Secret Data Api Decrypt Post",
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBasic": []
                    }
                ]
            }
        }
    }
}
```
____

## Задание 3. Подготовка к развертыванию (НЕОБЯЗАТЕЛЬНОЕ ЗАДАНИЕ):
Для запуска сервиса в production, обычно используются методы CI/CD, однако в данном случае мы не располагаем отдельными devops специалистами, поэтому для управщения задачи достаточно настроить `docker` образ.

Для выполнения этого задания необходимо приложить в проект Dockerfile, с помощью которого можно развернуть сервис.

Подробную информацию можно изучить на официальном сайте https://docs.docker.com/

____
`1:` Basic авторизация использует токен в виде зашифронваной строки `username:password` при помощи `base64` метода! Пример строки в заголовке `Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=`

`2:` Что касается документации, некоторые фреймворки могут генерировать ее "из коробки" на основе созданного API.