from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "genre": "Фантастика",
        "description": "Команда исследователей путешествует в космосе",
        "year": 2014,
        "rating": 8.7
    },
    {
        "id": 2,
        "title": "Матрица",
        "genre": "Фантастика, боевик",
        "description": "Узнать о природе",
        "year": 1999,
        "rating": 8.5
    },
    {
        "id": 3,
        "title": "Шрек",
        "genre": "Мультфильм",
        "description": "Спасение Фионы",
        "year": 2001,
        "rating": 8.1
    },
    {
        "id": 4,
        "title": "Титаник",
        "genre": "Драма",
        "description": "Любовь двух молодых людей",
        "year": 1997,
        "rating": 8.7
    },
    {
        "id": 5,
        "title": "Король Лев",
        "genre": "Мультфильм",
        "description": "Лев возвращает себе трон",
        "year": 1994,
        "rating": 8.5
    }
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404

if __name__ == "__main__":
    app.run(debug=True)
