import os
import json
from flask import Flask, render_template, jsonify, request, redirect, abort

app = Flask(__name__, static_url_path='/assets', static_folder='static')

@app.route('/pages/index.html')
def index():
    return render_template('index.html')
    
@app.route('/')
def index2():
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

# Download configuration - apenas filmes de domínio público ou com licença
DOWNLOADABLE_MOVIES = {
    # Exemplos de filmes de domínio público (IDs do TMDB)
    "872585": {  # Example ID - replace with actual public domain movies
        "title": "Exemplo de Filme Público",
        "legal_notice": "Este filme está em domínio público e pode ser baixado legalmente.",
        "qualities": [
            {"id": "720p", "name": "HD (720p)", "size": "1.2 GB"},
            {"id": "480p", "name": "SD (480p)", "size": "800 MB"}
        ]
    }
    # Adicione mais filmes aqui conforme necessário
    # Certifique-se de que tem direitos legais para distribuí-los
}

@app.route('/api/download-metadata')
def download_metadata():
    movie_id = request.args.get('id')
    
    if not movie_id:
        return jsonify({"error": "ID do filme não fornecido"}), 400
    
    if movie_id in DOWNLOADABLE_MOVIES:
        movie_data = DOWNLOADABLE_MOVIES[movie_id]
        return jsonify({
            "available": True,
            "title": movie_data["title"],
            "legal_notice": movie_data["legal_notice"],
            "qualities": movie_data["qualities"]
        })
    else:
        return jsonify({
            "available": False,
            "message": "Download não disponível para este filme.",
            "reason": "Apenas filmes em domínio público ou com licença estão disponíveis para download."
        })

@app.route('/download/<movie_id>')
def download_movie(movie_id):
    quality = request.args.get('q')
    
    if not quality:
        return jsonify({"error": "Qualidade não especificada"}), 400
    
    if movie_id not in DOWNLOADABLE_MOVIES:
        abort(404)
    
    # Verificar se a qualidade existe
    movie_data = DOWNLOADABLE_MOVIES[movie_id]
    quality_exists = any(q["id"] == quality for q in movie_data["qualities"])
    
    if not quality_exists:
        return jsonify({"error": "Qualidade não disponível"}), 400
    
    # Em uma implementação real, aqui você geraria uma URL assinada para o arquivo
    # Por enquanto, retornamos uma mensagem informativa
    return jsonify({
        "message": "Download seria iniciado aqui",
        "movie": movie_data["title"],
        "quality": quality,
        "note": "Esta é uma implementação demonstrativa. Em produção, seria redirecionado para o arquivo real."
    })

if __name__ == '__main__':
    port = 5000
    debug = True
    app.run(host='0.0.0.0', port=port, debug=debug)
