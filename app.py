import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello_world():
        return 'Hello_world'

    @app.route('/actors', methods=["POST"])
    def post_actor():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        try:
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            all_actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                "success": True,
                "actors": all_actors
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=["DELETE"])
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        try:
            actor.delete()
            all_actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                "success": True,
                "actors": all_actors
            })
        except Exception:
            abort(422)

    @app.route('/movies', methods=["POST"])
    def post_movie():
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)
        try:
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            all_movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                "success": True,
                "movies": all_movies
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=["DELETE"])
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        try:
            movie.delete()
            all_movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                "success": True,
                "movies": all_movies
            })
        except Exception:
            abort(422)

    @app.route('/movies',methods=["GET"])
    def get_movies():
        all_movies = [movie.format() for movie in Movie.query.all()]
        return jsonify({
            "success": True,
            "movies": all_movies
        })

    @app.route('/actors',methods=["GET"])
    def get_actors():
        all_actors = [actor.format() for actor in Actor.query.all()]
        return jsonify({
            "success": True,
            "actors": all_actors
        })

    @app.route('/actors/<int:actor_id>', methods=["PATCH"])
    def patch_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        try:
            body = request.get_json()
            actor.name = body.get('name', None)
            actor.gender = body.get('gender', None)
            actor.age = body.get('age', None)
            actor.update()
            all_actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                "success": True,
                "actors": all_actors
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=["PATCH"])
    def edit_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        try:
            body = request.get_json()
            movie.title = body.get('title', None)
            movie.release_date = body.get('release_date', None)
            movie.update()
            all_movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                "success": True,
                "movies": all_movies
            })
        except Exception:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessible(error):
        return jsonify({
            "success": False,
            'error': 422,
            'message': 'unprocessible'})

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            'error': 500,
            'message': 'internal server error'})

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            'error': 401,
            'message': 'unauthorized'})
    return app

app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)