"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return a movie by its id."""

    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    """Create and return a new rating."""

    # pass in user object, movie object, score integer
    # To test this function in the interactive mode, 
    # create the user and movie objects and then pass 
    # in those objects as the arguments
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)