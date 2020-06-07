import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello_world():
        return 'Welcome: This is my FSND Casting App.'

    # Implementing the end points
    @app.route('/actors', methods=["POST"])
    @requires_auth('post:actor')
    def post_actor(token):
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
    @requires_auth('delete:actor')
    def delete_actor(token, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
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
    @requires_auth('post:movie')
    def post_movie(token):
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
    @requires_auth('delete:movie')
    def delete_movie(token, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
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
    @requires_auth('get:movies')
    def get_movies(token):
        all_movies = [movie.format() for movie in Movie.query.all()]
        if len(all_movies) == 0:
            abort(422)
        return jsonify({
            "success": True,
            "movies": all_movies
        })

    @app.route('/actors',methods=["GET"])
    @requires_auth('get:actors')
    def get_actors(token):
        all_actors = [actor.format() for actor in Actor.query.all()]
        if len(all_actors) == 0:
            abort(422)
        return jsonify({
            "success": True,
            "actors": all_actors
        })

    @app.route('/actors/<int:actor_id>', methods=["PATCH"])
    @requires_auth('patch:actor')
    def patch_actor(token, actor_id):
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
    @requires_auth('patch:movie')
    def patch_movie(token, movie_id):
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

    # Implementing the error handlers
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
            'message': 'unprocessible'}),422

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            'error': 401,
            'message': 'unauthorized'}),401

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)