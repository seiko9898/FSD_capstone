import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie
from app import create_app

producer_header = {'Content-Type': 'application/json', 'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ims3aFU4b1ViTFBiNGdIUEotbjczcyJ9.eyJpc3MiOiJodHRwczovL3NlaWtvLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ5MTdjZWE0MDJlMjBiN2EwODg5YjEiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkxMjkwOTQyLCJleHAiOjE1OTEyOTgxNDIsImF6cCI6InBJbDY4ODExZmFXUkNxZDFWWTFJUTY5UTBxN3hjdHZ6Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.MMJyyw9CBynUD3HLJZQ2OyW2e8nlH3ZjbvmhoKDNFW4xBg9kfMBWJ2J7T14F1I0tk6HfP0i81LGtfhCabNdSqnhJJzMoyYy9pjWSa3kfy1fmEarELknICm16MmmLRxV_jp_bvThaXDeaYoPGxgSBN7pSzGfzcf57k1XDrYUpPsaN2AajYGi3RMFSexE0vvbKdVQw8n09dMOHPpjPMLJ5i28CYPqNqbznF094v6c7VQtuaiIqYfj3ZQdsvPBnK2xRsaRA4vmOzhA3Dm9hVE1_rpaiXhnm6lF32NM2NQmjjEuMg_0UogVKn1TW_gWX0gqMUhpAbgc5DzsRGmy2aueJ9Q'}
director_header = {'Content-Type': 'application/json', 'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ims3aFU4b1ViTFBiNGdIUEotbjczcyJ9.eyJpc3MiOiJodHRwczovL3NlaWtvLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ5MTc1ZmE0MDJlMjBiN2EwODg4ZTEiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkxMjkwODk2LCJleHAiOjE1OTEyOTgwOTYsImF6cCI6InBJbDY4ODExZmFXUkNxZDFWWTFJUTY5UTBxN3hjdHZ6Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.eXbNrs9s6JK9rmHOb6cdnlmUHfUoCx7BOctsAthSpo-ab7aYbJ53LDtIs06v0yGhhu2meakBfP2A7GMHirVPx5x3GUTUs8e2b_1HS7kN1nc-stTGC0se4Dzr2PFA9y_ZzMYpZs9VYRljrB_ooeWywLPc1CAdsZl22VMguMEAT-_nS13VWhr-QqCb5wJG7nvlpcggfkUTNso9r--QHRNxYDoXF3hmyQTSX3oENLEYtHn5gfKxubbYG_sQpVPSFYoaUSdXEmhabcD2rkvm-U8w36-v00wdanyln_cxTohLBsykOevBbnfG3yecfQ5yRiY8iFmDmFJI60bJMSV8GbNuTA'}
assistant_header = {'Content-Type': 'application/json', 'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ims3aFU4b1ViTFBiNGdIUEotbjczcyJ9.eyJpc3MiOiJodHRwczovL3NlaWtvLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQ5MzM0OTM4ZjA0NDBiOGQyYzMzMzgiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkxMjkyODIxLCJleHAiOjE1OTEzMDAwMjEsImF6cCI6InBJbDY4ODExZmFXUkNxZDFWWTFJUTY5UTBxN3hjdHZ6Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.KxTmmu0r9cFgqcEm5t3RhqEK3kmixrQSElXZTxIqSjEgBTNDEiguiQrY252xc96wpG0mfSuBJ2BT4kKcagKWIjDi1QIOjjKcIeyOzy0ke0phDHzgy2YPGEGav8GSYK6-ymoance1P_Inz6pePTYSC8vod5zaU8XKVLILCEwj4zhLV2jTdpz4M9tLgAhvxIVF0rINE5nP5nWto-FBWkwt8ifPmH5ycU-9nITyAdmux11AXsNN_Zd4o0Wsn_ZM2mQ-FOwwrhDLlkq5iNVWNq7reXMhvoGHjRl9Vt3UT8aWeck-vFXAySUtdqZqA2AlXy_qTIsLVSE1Fkl1JnaYzYXDnA'}


valid_actor = {'name': 'Barack Obama', 'age': 30, 'gender': 'male'}
invalid_actor = {'name': 'Barack Obama', 'age': 'Thirty', 'gender': 'male'}
valid_movie = {'title': 'Mission Possible', 'release_date':'2020-01-01'}
invalid_movie = {'title': 'Mission Impossible', 'release_date':'Twenty Twenty'}

class CastingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.drop_all()
            self.db.init_app(self.app)
            self.db.drop_all()
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors_422(self):
        res = self.client().get('/actors', headers = producer_header)
        self.assertEqual(res.status_code, 422)

    def test_get_actors_200(self):
        res = self.client().post('/actors', headers=producer_header, json=valid_actor)
        res = self.client().get('/actors', headers = producer_header)
        self.assertEqual(res.status_code, 200)

    def test_post_actor_200(self):
        res = self.client().post('/actors', headers=producer_header, json=valid_actor)
        self.assertEqual(res.status_code, 200)

    def test_post_actor_422(self):
        res = self.client().post('/actors', headers=producer_header, json=invalid_actor)
        self.assertEqual(res.status_code, 422)

    def test_get_movies_422(self):
        res = self.client().get('/movies', headers = producer_header)
        self.assertEqual(res.status_code, 422)

    def test_get_movies_200(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        res = self.client().get('/movies', headers = producer_header)
        self.assertEqual(res.status_code, 200)

    def test_post_movie_200(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        self.assertEqual(res.status_code, 200)

    def test_post_movie_422(self):
        res = self.client().post('/movies', headers=producer_header, json=invalid_movie)
        self.assertEqual(res.status_code, 422)

    def test_delete_actor_404(self):
        res = self.client().delete('/actors/10', headers=producer_header)
        self.assertEqual(res.status_code, 404)

    def test_delete_actor_200(self):
        res = self.client().post('/actors', headers=producer_header, json=valid_actor)
        res = self.client().delete('/actors/1', headers=producer_header)
        self.assertEqual(res.status_code, 200)

    def test_delete_movie_404(self):
        res = self.client().delete('/movies/10', headers=producer_header)
        self.assertEqual(res.status_code, 404)

    def test_delete_movie_200(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        res = self.client().delete('/movies/1', headers=producer_header)
        self.assertEqual(res.status_code, 200)

    def test_patch_actor_404(self):
        res = self.client().patch('/actors/10', headers=producer_header, json=valid_actor)
        self.assertEqual(res.status_code, 404)

    def test_patch_actor_200(self):
        res = self.client().post('/actors', headers=producer_header, json=valid_actor)
        res = self.client().patch('/actors/1', headers=producer_header, json=valid_actor)
        self.assertEqual(res.status_code, 200)

    def test_patch_movie_404(self):
        res = self.client().patch('/movies/10', headers=producer_header, json=valid_movie)
        self.assertEqual(res.status_code, 404)

    def test_patch_movie_200(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        res = self.client().patch('/movies/1', headers=producer_header, json=valid_movie)
        self.assertEqual(res.status_code, 200)

    # RBAC Assistant
    def test_assistant_get_movies_200(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        res = self.client().get('/movies', headers = assistant_header)
        self.assertEqual(res.status_code, 200)

    def test_assistant_post_movie_autherror(self):
        res = self.client().post('/movies', headers=assistant_header, json=valid_movie)
        data = json.loads(res.data)
        self.assertEqual(data['description'], "permission not found")

    # RBAC Director
    def test_director_delete_actor_200(self):
        res = self.client().post('/actors', headers=director_header, json=valid_actor)
        res = self.client().delete('/actors/1', headers=director_header)
        self.assertEqual(res.status_code, 200)

    def test_director_delete_movie_autherror(self):
        res = self.client().post('/movies', headers=producer_header, json=valid_movie)
        res = self.client().delete('/movies/1', headers=director_header)
        data = json.loads(res.data)
        self.assertEqual(data['description'], "permission not found")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()