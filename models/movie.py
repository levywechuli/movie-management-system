from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    release_year = Column(Integer, nullable=False)
    director = Column(String)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'))

    genre = relationship("Genre", back_populates="movies")

    def __init__(self, title, release_year, director, rating, genre):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.rating = rating
        self.genre = genre

    @classmethod
    def create(cls, session, title, release_year, director, rating, genre):
        new_movie = cls(title=title, release_year=release_year, director=director, rating=rating, genre=genre)
        session.add(new_movie)
        session.commit()

    @classmethod
    def delete(cls, session, movie_id):
        movie = session.query(cls).get(movie_id)
        if movie:
            session.delete(movie)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, movie_id):
        return session.query(cls).get(movie_id)