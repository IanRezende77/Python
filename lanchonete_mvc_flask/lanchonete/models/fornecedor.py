from . import db
from .base import BaseModel


class Fornecedor(BaseModel):
    """Tabela de fornecedores parceiros da lanchonete."""

    __tablename__ = "tabela_fornecedor"

    nome_empresa = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(25), nullable=False)
    produto_fornecido = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Fornecedor {self.nome_empresa}>"
