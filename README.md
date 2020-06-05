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
pip install foobar
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

### Hosting Instructions

To run the local server run the following commands from the source directory:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Backend

### Models
**Actor**: The database table Actor has attributes name, age and gender
**Movie**: The database table Movie has attributes title and release date

### Roles:

**Casting Assistant**: Can view actors and movies

**Casting Director**All permissions a Casting Assistant has and…

Add or delete an actor from the database

Modify actors or movies

**Executive Producer**All permissions a Casting Director has and…

Add or delete a movie from the database

### API Endpoints

**GET /actors**
curl --location --request GET 'https://castingagencyfsnd.herokuapp.com/movies' \
--header 'Authorization: Bearer '

```bash
curl --location --request GET 'https://casting9898.herokuapp.com/actors' \
--header 'Authorization: Bearer YOUR_VALID_JWT_TOKEN'
```
Returns

```bash
{
  "actors": [
    {
      "age": 45, 
      "gender": "male", 
      "id": 1, 
      "name": "brad pitt"
    }
  ], 
  "success": true
}
```

**GET /movies**

**DELETE /actors**

**DELETE /movies**

**POST /actors**

```bash
{
  "actors": [
    {
      "age": 45, 
      "gender": "male", 
      "id": 1, 
      "name": "brad pitt"
    }
  ], 
  "success": true
}
```

**POST /movies**

**PATCH /actors**

**PATCH /movies**
