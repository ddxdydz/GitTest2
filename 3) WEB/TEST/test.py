from flask import Flask, url_for, request, render_template

app = Flask(__name__)
# Эта настройка защитит наше приложение от межсайтовой подделки запросов.
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = dict()
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('JINJA_TEST.html', **param)


if __name__ == '__main__':  # http://127.0.0.1:8000/
    app.run(port=8000, host='127.0.0.1')
