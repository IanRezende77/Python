from . import db
from .base import ModeloBase
class Jogador(ModeloBase):
 __tablename__="jogadores"
 nome=db.Column(db.String(100));posicao=db.Column(db.String(50));clube=db.Column(db.String(100));cabeceio=db.Column(db.Integer);forca=db.Column(db.Integer)
 @classmethod
 def listar(cls): return cls.query.all()