from db import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class Game(db.Model):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    time = Column(DateTime)
    sent_alert = Column(Boolean)
    
    def __repr__(self):
        return "<Game(name='{}' @ time='{}') [sent={}]>"\
                .format(self.name, self.time, self.sent_alert)

    @staticmethod
    def create_game(game):
        new_game = Game(
            name=game["name"],
            time=game["time"],
            sent_alert=False
        )

        db.session.add(new_game)
        db.session.commit()

        return new_game

    @staticmethod
    def mark_as_alerted(gameId):
        db.session.query(Game).filter(Game.id==gameId).update({Game.sent_alert: True})
        db.session.commit()

        return "ok"