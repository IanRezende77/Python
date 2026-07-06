from . import db
from .base import BaseModel


class Cliente(BaseModel):
    """Tabela de clientes da lanchonete."""

    __tablename__ = "tabela_cliente"

    nome = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)
    pontos_fidelidade = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Cliente {self.nome}>"
