# 1. Цель проекта
Цель проекта - разработать систему для отслеживания пользователями(далее Проходжембцы) пройденных игр, просмотренных фильмах, сериалах и аниме(далее Система).

# 2. Описание системы
Система состоит из следующих функциональных блоков:
1. Регистрация, аутентификация и авторизация
2. Функционал для проходжембцев
3. Функционал для тайтлов
4. Функционал для прохождений
5. Функционал для отзывов
6. Уведомления о критических ошибках в email

## 2.1 Регистрация, аутентификация и авторизация
Аутентификация будет проходить по принципу Token-Based Authentication
[Описание](https://gist.github.com/zmts/802dc9c3510d79fd40f9dc38a12bccfc)

Все действия в приложения могут выполнять только авторизованные пользователи.

### 2.1.1 Регистрация
Пользователь отправляет запрос на регистрацию с email для валидации. После ему на почту приходит код для проверки email.

При регистрации нового проходжембца должны быть запрошены следующие поля:
- email
- username
- password
- code - код, отправленный по email

### 2.1.2 Аутентификация
При аутентификации проходжембца должны быть запрошены следующие поля:
- email
- password

В результате возвращаются access токен, refresh токен и время истечения жизни access токена в формате UNIX timestamp.

### 2.1.3 Авторизация
Все запросы пользователя приложение делает с access токеном в заголовках (Authorization: Bearer <Токен>)

Access токен имеет ограниченное время жизни, когда приложение делает запрос с устаревшим токеном, то Система отправляет предупреждение.

Для обновления устаревшего access токена нужно отправить запрос на обновление со следующими полями:
- refresh_token - содержит refresh токен, выданный при регистрации, входе или предыдущем обновлении токенов.

### 2.1.5 Восстановление пароля
Сначала отправляется запрос на смену пароля, на почту отправляется код для подтверждения.

При восстановлении пароля должны быть запрошены следующие поля:
- email
- code - код, отправленный по email

После пользователь отправляет новый пароль с кодом подтверждения 

### 2.1.6 Изменение пароля
При изменении пароля должны быть запрошены следующие поля:
- current_password
- new_password

### 2.1.7 Изменение текущей почты
Сначала отправляется запрос на смену почты с указанием нового email,  на почту отправляется код для подтверждения.

Далее должны быть запрошены следующие поля:
- email - новый email
- password - пароль
- code - код, отправленный на новую почту

## 2.3 Функционал для проходжембцев
Профиль проходжембца будет состоять из нескольких таблиц. Основная это user, где будут храниться данные для авторизации:
- id
- email
- password_hash
- joined_at - дата регистрации
- last_auth_at - дата последнего входа

В дополнительной(profile) будет храниться вся остальная информация о пользователе:
- username
- avatar
- возможно ссылки на профили в разных соцсетях

### 2.3.1 Просмотр профиля
Если пользователь запрашивает свой профиль то ему выдается полная информация, то выдаваемая информация включает в себя email.

В профиле сверху указывается аватар и имя пользователя, чуть ниже отображается дополнительная информация. 

### 2.3.2 Пользовательские прохождения
Прохождения деляться по группам тайтлов, изначально сортировка по дате последнего обновления. Можно фильтровать по статусу(статус выбирается в отдельном пункте меню).

Так-же при просмотре прохождений нам доступна информация и о тайтле.

### 2.3.3 Пользовательские отзывы
Отзывы сортируются по дате последнего обновления, можно фильтровать по группам тайтлов.

Отзывы, отображаемые в профиле содержат в себе информацию о тайтле.

### 2.3.4 Редактирование профиля
Настройки отдельный пункт где пользователю доступны смена текущей почты, пароя, имени и всякой дополнительнйо информации.

## 2.4 Функционал для тайтлов
Таблица тайтла состоит из следующих полей:
- id
- name - Название тайтла
- cover - Обложка тайтла
- description - Описание тайтла
- type - Тип тайтла - Выбирается из константных значений(напр. Игра, Фильм, Сериал, Аниме)
- release_year - Год релиза
- rating - средний рейтинг

### 2.4.1 Просмотр списка тайтлов
Тайтлы делятся по группам, нельзя запрашивать тайтлы, принадлежащие разным группам кучей.
Список тайтлов выдается постранично, по умолчанию все сортируется по id. Так-же доступен поиск по имени и сортировка по году релиза и рейтингу.

### 2.4.2 Просмотр информации о тайтле
На основной странице тайтла доступна обложка, название и группа. Чуть ниже отображается описание. 

Показ статуса прохождения если такой имеется, иначе выбор статуса.
ТОже самое с отзывом


### 2.4.3 Добавление информации о тайтле
При создании новой записи о тайтле должны быть запрошены следующие поля:
- name
- description
- type
- release_year

### 2.4.4 Редактирование информации о тайтле
При редактировании текущей записи должны быть запрошены следующие поля:
- name
- description
- type 
- release_year

Изменение обложки тайтла выполняется отдельно.

### 2.4.5 Удаление тайтла
Для удаления тайтла достаточно передать его id.

### 2.4.6 Просмотр отзывов на тайтл
Отзывы сортируются по дате последнего обновления, также можно отсортировать по рейтингу.

Отзывы содержат в себе информацию о пользователе.

### 2.4.7 Просмотр прохождений тайтла
Прохождения сортируются по дате последнего обновления. Можно фильтровать по статусу(статус выбирается в отдельном пункте меню).

Так-же при просмотре прохождений нам доступна информация и пользователе.

## 2.5 Функционал для прохождений
Таблица прохождений состоит из следующих полей:
- id
- title_id - отсылается к тайтлу, который отметил проходжембец
- user_id - отсылается к проходжембцу, который отметил тайтл
- state - состояние прохождения - выбирается из константных значений (В процессе, Пройдено, 100%)
- updated_at - дата последнего обновления
- Тайтл и пользователь для каждого прохождения должны быть уникальны.

### 2.5.1 Добавление прохождения
При добавлении прохождения должны быть запрошены следующие поля:
- title_id
- state

### 2.5.2 Редактирование прохождения
Для редактирования прохождения должны быть запрошены следующие поля:
- state

### 2.5.3 Удаление прохождения
Для удаления прохождения достаточно передать его id. Удалять можно только собственные прохождения.

## 2.6 Функционал для отзывов
Таблица отзывов состоит из следующих полей:
- id
- title_id - отсылается к тайтлу, который отметил проходжембец
- user_id - отсылается к проходжембцу, который отметил тайтл 
- rating - Оценка пользователя (0-100)    
- text - Текстовый обзор пользователя
- updated_at - дата последнего обновления
- Тайтл и пользователь для каждого отзыва должны быть уникальны.

*При любом взаимодействии с отзывом обновляется рейтинг тайтла.

### 2.5.1 Добавление отзыва
При добавлении отзыва должны быть запрошены следующие поля:
- title_id
- rating - число от 0 до 100.
- text - текстовое обоснование оценки.

### 2.5.2 Редактирование отзыва
При редактировании отзыва должны быть запрошены следующие поля:
- rating
- text

### 2.5.3 Удаление отзыва
Для удаления отзыва достаточно передать его id. Удалять можно только собственные отзывы.

# 3. Предполагаемый стек технологий
Для реализации системы предполагается использовать следующие технологии:
- Бэкенд
    - Язык Python
    - FastAPI фреймворк 
    - БД PostgreSQL
    - SQLAlchemy ORM
    - Alembic для миграций
    - Redis для временного хранения токенов
    - Aioredis для взаимодействия с Redis
    - aiosmtplib для работы с электронной почтой

- Фронтенд
    - Язык JavaScript
    - Vue

- Android клиент
    - Язык Dart
    - Flutter

# 4. Требования к дизайну
Он должен быть.


# 5. Список URL API
/api/v1/ - основной url для отправки запросов на сервер

## 5.1. Авторизация
POST /auth/signin - регистрация
POST /auth/token - получение пары токенов авторизации
POST /auth/token/update - обновление токенов
POST /auth/email/change - изменение текущей почты
POST /auth/email/validate - запрос на отправку кода проверки email
POST /auth/password/change - изменение пароля
POST /auth/password/restore - востановление забытого пароля

## 5.2. Профиль
GET|PATCH /user/@me - получение информации о текущем пользователе | Редактирование пользователя
POST /user/@me/avatar - изменение аватара пользователя
GET /user/{user_id} - получение информации о пользователе
GET /user/{user_id}/walks - полученение прохождений пользователя
GET /user/{user_id}/reviews - получение обзоров пользователя 

## 5.3. Тайтлы
GET|POST /titles - получение страницы с тайтлами | Создание тайтла
PATCH /titles/{title_id} - редактирование информации о тайтле
POST /titles/{title_id}/cover - добавление или редактирование обложки тайтла
DELETE /titles/{title_id} - удаление тайтла

GET /titles/{title_id}/reviews - получение пользовательских отзывов на тайтл
GET /titles/{title_id}/walks - получение прохождений

## 5.4. Прохождения
POST|PATCH /walks - создание или редактирование прохождения
DELETE /walks/{walk_id} - удаление прохождения

## 5.6. Отзывы
POST|PATCH /walks - создание или редактирование прохождения
DELETE /walks/{walk_id} - удаление прохождения
