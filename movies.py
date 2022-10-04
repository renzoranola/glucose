from flask import Flask, jsonify, request

app = Flask(__name__)
movies = [ 

    {
        "name": "Little women",
        "casts": ["Lee","Kim"],
        "genres": ["Drama","Thriller"]
    },
    {
        "name": "Malaala mo kaya the Movie",
        "casts": ["Boy Abunda","Vice Ganda"],
        "genres": ["Drama","Biography"]
    }
]
@app.route('/movies', methods=['GET'])
def displayMovies():
    return jsonify(movies)

if __name__== '__main__':
    app.run()
