from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    movies = relationship("Movie", back_populates="genre")

    @classmethod
    def create(cls, session, name):
        new_genre = cls(name=name)
        session.add(new_genre)
        session.commit()

    @classmethod
    def delete(cls, session, genre_id):
        genre = session.query(cls).get(genre_id)
        if genre:
            session.delete(genre)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, genre_id):
        return session.query(cls).get(genre_id)