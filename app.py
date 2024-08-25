from flask import Flask, render_template  # render_template нужен для отображения HTML-шаблонов.

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Маршрут для страницы с рецептом бургера
@app.route('/burger')
def burger():
    return render_template('recipes/burger.html')

# Маршрут для страницы с рецептом стейка
@app.route('/steak')
def steak():
    return render_template('recipes/steak.html')

# Маршрут для страницы с рецептом пирожного
@app.route('/cake')
def cake():
    return render_template('recipes/cake.html')

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем сервер Flask в режиме отладки.
