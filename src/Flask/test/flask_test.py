from flask import Flask, json, render_template

app = Flask(__name__)

d = {'1': 'Hello', '2': 'World', '3': 'Python', '4': 'Dictionary'}


@app.route('/api')
def api():
    return json.jsonify(d)


class Items():
    def __init__(self, num, name):
        self.num = num
        self.name = name


t = [Items(x, x * 2) for x in range(5)]


@app.route('/')
def index():
    return render_template('index.html', items=t)


if __name__ == '__main__':
    app.run(debug=True)
