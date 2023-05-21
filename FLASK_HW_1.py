from flask import Flask
from flask import render_template

'''

'''


app = Flask(__name__)

_HomeTask_1 = [

              {"Header": {"name1": "Главная", "name2": "Контакты", "name3": "О нас"},
              "Menu": {"item1": "Проблема с налогами", "item2": "Проблема с людьми", "item3": "Проблема с недвижкой"},
              "Footer": "Это главная страница"},
              {"Header": {"name1": "Контакты", "name2": "Главная", "name3": "О нас"},
              "Menu": {"item1": "Телефон: '89000000001'", "item2": "Почта: FSB@mail.ru", "item3": "inst: FSB.REELS"},
              "Footer": "Это страница Контакты"},
              {"Header": {"name1": "О нас", "name2": "Главная", "name3": "Контакты"},
              "Menu": {"item1": "Адрес: Лубянка, 9", "item2": "Кол-во работников: 430", "item3": "Компания: 'ФСБ'"},
              "Footer": "Это страница О нас"}

]

_HomeTask_2 = [

            {"Header": {"name1": "Одежда", "name2": "Обувь", "name3": "Куртка"},
             "Menu": {"item1": "МУЖЧИНЫ", "item2": "ЖЕНЩИНЫ", "item3": "ДЕТИ"},
             "Footer": "Это главная Одежда"},
            {"Header": {"name1": "Обувь", "name2": "Куртка", "name3": "Одежда"},
             "Menu": {"item1": "МУЖЧИНЫ", "item2": "ЖЕНЩИНЫ", "item3": "ДЕТИ"},
             "Footer": "Это страница Обувь"},
            {"Header": {"name1": "Куртка", "name2": "Одежда", "name3": "Обувь"},
             "Menu": {"item1": "МУЖЧИНЫ", "item2": "ЖЕНЩИНЫ", "item3": "ДЕТИ"},
             "Footer": "Это страница Куртка"}

]



@app.route('/FlaskHome1/')
def flaskhome_1_1():
    return render_template('HomeWork_1_task_1.html', HomeTask_1=_HomeTask_1)


@app.route('/FlaskHome2/')
def flaskhome_1_2():
    return render_template('HomeWork_1_task_2.html', HomeTask_1=_HomeTask_2)


if __name__ == '__main__':
    app.run()

