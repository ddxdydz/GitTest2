"""
# встроенный CGI сервер (стандарт интерфейса, применяемого для связи внешней программы с веб-сервером).
# ПРИМЕР СОЗДАНИЯ СЕРВЕРА:
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 25565)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)  httpd.serve_forever()

# http://localhost:25565/cgi-bin/index.py  # localhost (или 127.0.0.1)
Адрес в командной строке localhost (или 127.0.0.1) — это адрес вашего компьютера + номер порта.
* Номер порта — целое число от 0 до 65536.
* Стандартные порты для HTTP: 80, 8000 и 8080.
"""

from flask import Flask, url_for, request, render_template, redirect, make_response, abort
# request - хранит всю информацию о пользовательском запросе
# url_for - правильная ссылка
# render_template - обработчик шаблонов
# make_response - тоже что и return 'MESSS"
# redirect - для перенаправки пользоваткля (redirect('/success'))
# abort - оборвать

'''
* Статический контент Flask по умолчанию ищет в директории static. 
Рекомендуется создавать подпапки в static для каждого типа статического контента (static/fonts; /img; /css и т. д.)
'''
'''
* HTML-шаблоны во Flask записываются как отдельные файлы, хранящиеся в папке templates, 
которая находится (по умолчанию) в корневой папке приложения (base.html, auto_answer.html).
'''

app = Flask(__name__)   # объект приложения
# Эта настройка защитит наше приложение от межсайтовой подделки запросов.
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
i = 0


# Декораторы используются для регистрации нашей функции, как функции обратного вызова для определенных событий.
# Создается связь между адресом (URL) в браузере ('/' и '/index') и функцией index
# Когда веб-браузер запрашивает один из этих двух URL-адресов, Flask будет вызывать эту функцию
# и передать возвращаемое значение обратно в браузер в качестве ответа.
@app.route('/')  # http://127.0.0.1:8080
@app.route('/index')  # http://127.0.0.1:8080/index
@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    return '</br>'.join(countdown_list)

    # return '''<img src="{url_for('static', filename='img/riana.jpg')}" alt="картинка не нашлась">'''

    # style.css: h1 {color: #d22e3a}
    # return f"""<!doctype html>
    #             <html lang="en">
    #               <head>
    #                 <meta charset="utf-8">
    #                 <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    #                 <title>Привет, Яндекс!</title>
    #               </head>
    #               <body>
    #                 <h1>Первая HTML-страница</h1>
    #               </body>
    #             </html>"""


# app.route принимет значение 1 или более параметров(пишется после завершающего слэша внутри треугольных скобок <>):
#     Имя конвертера - Описание
# string - (по умолчанию) любой текст без слешей
# path - строка, но может содержать слеши, для передачи некоторого URL-пути
# int - положительное целое число
# float - положительное дробное число
# uuid	стандарт строк-идентификаторов из 16 байт в шестнадцатеричном представлении.550e8400-e29b-41d4-a716-44665544000
@app.route('/two_params/<username>/<int:number>')
def two_params(username, number):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h2>{username}</h2>
                    <div>Это первый параметр и его тип: {str(type(username))[1:-1]}</div>
                    <h2>{number}</h2>
                    <div>Это второй параметр и его тип: {str(type(number))[1:-1]}</div>

                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>

                  </body>
                </html>'''


# * Bootstrap — это свободный набор инструментов для создания сайтов и веб-приложений,
# который включает в себя скрипты, стили, иконки и многое другое.  https://getbootstrap.com/
# Подключение состоит из: - Подключение стилей - Подключение JavaScript
# Форма с распространенными типами полей ввода, для их стилизации используем Bootstrap.

# списком методов протокола HTTP, с которыми он работает:
# GET — запрашивает данные, не меняя состояния сервера («прочитать»).
# POST — отправляет данные на сервер («отправить»).
# PUT — заменяет все текущие данные сервера данными запроса («заменить»).
# DELETE — удаляет указанные данные («удалить»).
# PATCH — используется для частичного изменения данных («изменить»).
@app.route('/form_sample', methods=['POST', 'GET'])  # списком методов протокола HTTP, с которыми он работает
def form_sample():
    '''style.css:
    form.login_form {
        margin-left: auto;
        margin-right: auto;
        max-width: 450px;
        background-color: #ffcc00;
        border: 1px solid gray;
        border-radius: 5px;
        padding: 10px;}'''
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">

                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>

                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>

                                    <button type="submit" class="btn btn-primary">Записаться</button>

                                </form>

                                <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>

                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        # корректная обработка значения чекбокса будет выглядеть так: request.form.get('accept')
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])

        # enctype="multipart/form-data" - для чтения файлов
        f = request.files['file']
        print(f.read())

        return "Форма отправлена"
    '''
     * Какие типы элементов ввода поддерживает HTML:
    button — кнопка
    checkbox — множественный выбор
    color — поле выбора цвета
    date, datetime, datetime-local, month, time, week — ввод даты и времени
    email — поле для ввода адреса электронной почты
    file — поле для выбора файла
    number — поле для ввода числовой информации
    password — поле для ввода пароля
    radio — выбор одного из нескольких вариантов
    range — ползунок (как в музыкальном или видео-плеере)
    submit — кнопка для отправки формы
    tel — поле для ввода телефона
    text — поле для ввода текста
    url — поле для ввода адреса в Интернете
    '''


# Операция, которая преобразует шаблон в HTML-страницу, называется рендерингом.
# Механизм шаблонов, встроенный во Flask, называется Jinja2.
# все блоки {{...}} в нем заменяются фактическими значениями переданных аргументов.
# Шаблонизатор Flask поддерживает условные операторы, заданные внутри блоков {% ...%}.
@app.route('/index_render')
def index_render():
    param = dict()
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)  # HTML-шаблон
    # return render_template('index.html', title='страница', username="Ученик")

    # Эта функция принимает имя файла шаблона и перечень аргументов шаблона и возвращает тот же шаблон
    # По умолчанию параметры шаблона - пустые строки.
    # Кроме переданных параметров внутри шаблона мы имеем доступ и к служебным объектам. Например, request, или session.


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
