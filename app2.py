from flask import Flask, render_template
import os
def index():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('index2.html') #змінити потім на index2


folder = os.getcwd() # запам'ятали поточну робочу папку
# Створюємо об'єкт веб-додатку:
app = Flask(__name__, template_folder=folder, static_folder=folder)
#перший параметр - ім'я модуля
# параметр з ім'ям static_folder визначає ім'я папки, що містить статичні файли
# параметр з ім'ям template_folder визначає ім'я папки, що містить шаблони


# створюємо правило дляURL '/':
app.add_url_rule('/', 'home', index)

if __name__ == "__main__":
    # Запускаємо веб-сервер:
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
