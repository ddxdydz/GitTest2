import datetime
from flask import Flask, request, session, url_for, render_template, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# По умолчанию сессии существуют до тех пор, пока пользователь не закроет браузер.
session.permanent = True  # жизни сессии будет продлен до 31 дня
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)


@app.route("/cookie_test")  # http://127.0.0.1:5000/cookie_test
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1), max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response("Вы пришли на эту страницу в первый раз за последние 2 года")
        # res = make_response(render_template("index.html", news=news))
        res.set_cookie("visits_count", '1', max_age=60 * 60 * 24 * 365 * 2)
        # имя куки, значение, а также максимальное время жизни
        # у куки ключи - тип str, значения — тип str или bytes.

        # Удаление куки: res.set_cookie("visits_count", '1', max_age=0)
    return res


# Сессии во Flask: не могут быть изменены пользователем(если у него нет нашего секретного ключа).
# Сессии также хранятся в куках, но в зашифрованном виде.
@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(f"Вы пришли на эту страницу {visits_count + 1} раз")
    # session.pop('visits_count', None) - Удаление сессий


if __name__ == '__main__':  # http://127.0.0.1:5000/
    app.run(port=5000, host='127.0.0.1')
