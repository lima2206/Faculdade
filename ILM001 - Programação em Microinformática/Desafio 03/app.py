from flask import Flask, render_template, url_for

app = Flask(__name__, )

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/quem-somos')
def quemsomos():
    return render_template('quem-somos.html')