from datetime import datetime
from . import db


class BaseModel(db.Model):
    """Modelo abstrato com campos comuns para todas as tabelas locais."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    data_atualizacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def excluir(self):
        db.session.delete(self)
        db.session.commit()
