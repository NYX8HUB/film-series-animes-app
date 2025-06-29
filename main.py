from flask import Flask, render_template

app = Flask(__name__, static_url_path='/assets', static_folder='static')

@app.route('/pages/index.html')
def index():
    return render_template('index.html')

@app.route('/pages/busca.html')
def pag1():
    return render_template('pages/busca.html')

@app.route('/pages/filme.html')
def pag2():
    return render_template('pages/filme.html')

@app.route('/pages/serie.html')
def pag3():
    return render_template('pages/serie.html')

@app.route('/pages/anime.html')
def pag4():
    return render_template('pages/anime.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
