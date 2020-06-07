# Full Stack project: Casting Agency

## Motivation for the Project.
This project provides the endpoints to create a Casting agency website. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

## Setting up the Project

### Python
The project uses python 3.7. 

### Virtual Environment
To keep the dependencies separate for each project, please create a virtual environment for local development and testing

```bash
python -m venv env
source env/bin/activate
```

### Project Dependencies

With python installed and virtual environment created, run the following command to install all the dependencies:

```bash
pip install -r requirements.txt
```

**Flask**: Flask is a micro web framework written in Python. Flask supports extensions that can add application features as if they were implemented in Flask itself.

**Flask-Cors**: A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

**Flask-Migrate**: Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface or through the Flask-Script extension.

**SQLAlchemy**: SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

**Psycopg2**: Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety

### Creating Database
To create a Postgres Database run:

```bash
createdb casting
```

### Hosting Locally
To run the local server run the following commands from the source directory:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Cloud Hosting

The app is hosted on Heroku under:

https://casting9898.herokuapp.com/

## Running Tests

THE JWT in the test_App.py have to be filled in with a valid JWT. From the source folder run the following commands:
```bash
python test_app.py
```
## Backend

### Models
**Actor**: The database table Actor has attributes name, age and gender

**Movie**: The database table Movie has attributes title and release date

### RBAC Roles:

**Casting Assistant**: Can view actors and movies

**Casting Director**: All permissions a Casting Assistant has and…

Add or delete an actor from the database

Modify actors or movies

**Executive Producer**: All permissions a Casting Director has and…

Add or delete a movie from the database

### API Endpoints

**GET /actors**

```bash
curl --location --request GET 'https://casting9898.herokuapp.com/actors' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```
Returns:

A JSON object of all the actors in the database.

**GET /movies**
```bash
curl --location --request GET 'https://casting9898.herokuapp.com/movies' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the movies in the database.

**DELETE /actors**
```bash
curl --location --request DELETE 'https://casting9898.herokuapp.com/actors/1' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the actors in the database.

**DELETE /movies**
```bash
curl --location --request DELETE 'https://casting9898.herokuapp.com/movies/1' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the movies in the database.

**POST /actors**

```bash
curl --location --request POST 'https://casting9898.herokuapp.com/actors' \
application/json" -d'{"name":"Angelina Jolie", "age":"40", "gender":"Female"}' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the actors in the database.

**POST /movies**
```bash
curl --location --request POST 'https://casting9898.herokuapp.com/movies' \
-H"Content-Type: application/json" -d'{"title":"Fury", "release_date":"2019-01-01"}' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the movies in the database.

**PATCH /actors**
```bash
curl --location --request POST 'https://casting9898.herokuapp.com/actors/1' \
application/json" -d'{"name":"Brad Pitt", "age":"50", "gender":"Male"}' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the actors in the database.

**PATCH /movies**
```bash
curl --location --request POST 'https://casting9898.herokuapp.com/movies/1' \
-H"Content-Type: application/json" -d'{"title":"Matrix", "release_date":"2005-01-01"}' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```

Returns:

A JSON object of all the movies in the database.

## Error handlers

The following error handlers have been implemented:

**422**: Unprocessible

**404**: Not Found

**Auth Error**: Authorization or permission errors