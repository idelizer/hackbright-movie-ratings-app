"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')


model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = ['poster_path']

    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    movies_in_db.append(crud.create_movie(title, overview, release_date, poster_path)) 
    
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    new_user = crud.create_user(email, password)

    for n in range(10):
        a_score = randint(1, 5)
        a_movie = choice(movies_in_db)
        crud.create_rating(new_user, a_movie, a_score)
        




