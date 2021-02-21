from db import db
from sqlalchemy import Column, Integer, String, Date, DateTime

class Game(db.Model):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    time = Column(DateTime)
    
    def __repr__(self):
        return "<Game(name='{}' @ time='{}')>"\
                .format(self.name, self.time)

    @staticmethod
    def create_game(game):
        new_game = Game(
            name=game["name"],
            time=game["time"]
        )

        db.session.add(new_game)
        db.session.commit()

        return new_game