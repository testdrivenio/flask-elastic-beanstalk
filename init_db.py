from datetime import date

from app import db
from app import Movie

db.create_all()

if Movie.query.count() == 0:
    movies = [
        Movie(title='Fight Club', release_date=date(1999, 9, 15)),
        Movie(title='The Matrix', release_date=date(1999, 3, 31)),
        Movie(title='Donnie Darko', release_date=date(2001, 1, 19)),
        Movie(title='Inception', release_date=date(2010, 7, 16)),
    ]

    for movie in movies:
        db.session.add(movie)

    db.session.commit()
