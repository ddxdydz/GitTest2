'''
* Для каждого из атрибутов типа sqlalchemy.Column будет создан одноименный столбец в базе данных согласно его описанию:
sqlalchemy.Integer (sqlalchemy.String, sqlalchemy.DateTime и т. д.) — указания типа данных
primary_key=True — столбец является первичным ключом (числовой идентификатор - однозначно идентифицирует каждую запись в таблице).
autoincrement=True — признак автоинкрементного поля. Увеличение значения первичного ключа на единицу при вставке каждой новой записи.
nullable=True/False — может ли поле не содержать никакой информации и быть пустым
unique=True/False — содержит ли поле только уникальные значения или они могут повторяться
default=datetime.datetime.now — значение по умолчанию. Момент создания пользователя.
index=True — создать индекс по этому полю. Индекс, если говорить упрощенно, позволяет значительно повысить скорость
    поиска по одному или нескольким полям базы данных. Цена этого — уменьшение скорости вставки данных, поэтому не стоит
    делать индексы на абсолютно все поля, а только на те (и ту их комбинацию), по которым будет часто осуществляться поиск
'''

'''
db_session.global_init("db/blogs.db")
db_sess = create_session()
for user in db_sess.query(User).filter(User.age < 18):
    print(user, user.age, 'years')


user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
db_sess = db_session.create_session()
# добавление объектов
db_sess.add(user)  
db_sess.commit()

#  параметр - классы объектов, которые мы хотим достать.
user = db_sess.query(User).first()  # получение данных
print(user.name)
#  пройдемся вообще по всем пользователям в таблице
for user in db_sess.query(User).all():
    print(user)
    for news in user.news:
        print(news)
for user in db_sess.query(User).all(User.id, User.name):
    print(user)

# Метод filter() - результаты с помощью оператора WHERE. Он принимает колонку, оператор или значение.
# отфильтруем пользователей и выберем только тех, у которых id > 1, а почта не содержит 1.
for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
    print(user)
# Условия в скобках соединяются в запросе через AND.
# Давайте изменим запрос, чтобы условия фильтра соединялись через OR:  скобки вокруг частей фильтра обязательны.
for user in db_sess.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
    print(user)
# Операция : Снитаксис ORM
# EQUALS - NOT EQUAL	query(User).filter(User.name == 'Иван')
# LIKE - NOT LIKE	query(User).filter(User.name.like('%Иван%'))
# IN - NOT IN	query(User).filter(User.name.in_(['Иван', 'Петр', 'Максим'])) - User.name.notin_ или ~User.name.in_
# NULL	query(User).filter(User.name == None)
# AND	query(User).filter(User.name == 'Иван', User.id > 3) или filter(User.name == 'Иван').filter(User.id > 3)
# OR	query(User).filter((User.name == 'Иван') | (User.id > 3)) или filter(or_(User.name == 'Иван', User.id > 3))

# Изменение записи
user = db_sess.query(User).filter(User.id == 1).first()  # выбрать нужную запись
print(user)
user.name = "Измененное имя пользователя"  # поменять нужные атрибуты
user.created_date = datetime.datetime.now()
db_sess.commit()  # вызвать у сессии метод commit

# Удаление
db_sess.query(User).filter(User.id >= 3).delete()
db_sess.commit()
# Удаление конкретного пользователя
user = db_sess.query(User).filter(User.id == 2).first()
db_sess.delete(user)
db_sess.commit()

# Добавление записи пользователю:
# Мы можем создать объект класса News и заполнить его поля, в том числе указать явно id записи автора:
news = News(title="Первая новость", content="Привет блог!", user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()
# Можем в качестве user указать объект класса User, выбранный (или созданный) заранее:
user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Вторая новость", content="Уже вторая запись!", user=user, is_private=False)
db_sess.add(news)
db_sess.commit()
# через объект класса User мы можем взаимодействовать с его записями в таблице News почти как со списком:
user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная", is_private=True)
user.news.append(news)
db_sess.commit()
'''
