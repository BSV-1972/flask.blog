from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():

    return render_template("index.html", title="Главная")



if __name__ == '__main__':
    app.run(debug=True, port=5656)  # стандартный порт у Фласка 5000, у Джанга 8000