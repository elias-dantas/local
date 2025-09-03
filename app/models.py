# models.py (SQLAlchemy para Flask)

from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    endereco = db.Column(db.String(200))

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    quantidade_disponivel = db.Column(db.Integer, default=0)
    preco_locacao = db.Column(db.Float)

class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    data_emissao = db.Column(db.DateTime, default=db.func.current_timestamp())
    total = db.Column(db.Float)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    orcamento_id = db.Column(db.Integer, db.ForeignKey('orcamento.id'))
    data_confirmacao = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # Ex: "Confirmado", "Pendente"