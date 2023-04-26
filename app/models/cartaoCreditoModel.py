from ..database import db
from flask_login import UserMixin

class CartaoCredito(db.Model, UserMixin):
    __tablename__ = 'tb_cartao_credito_ccr'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_cartao_credito_ccr', db.Integer, autoincrement=True, primary_key=True)
    txtNumero = db.Column('txt_numero_ccr', db.String(16), nullable=False, unique=True)
    txtNome = db.Column('txt_nome_ccr', db.String(16), nullable=False, unique=True)
    txtValidade = db.Column('txt_validade_ccr', db.String(16), nullable=False, unique=True)
    txtCVC = db.Column('txt_cvc_ccr', db.String(16), nullable=False, unique=True)
    datInicio = db.Column('dat_inicio_ccr', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_ccr', db.DateTime, nullable=True)