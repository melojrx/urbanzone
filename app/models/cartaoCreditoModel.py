from app.models.userModel import User
from ..database import db

class CartaoCredito(db.Model):
    __tablename__ = 'tb_cartao_credito_ccr'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_cartao_credito_ccr', db.Integer, autoincrement=True, primary_key=True)
    idUsuario = db.Column('id_usuario_ccr', db.Integer, db.ForeignKey(User.id), nullable=False)
    txtNumero = db.Column('txt_numero_ccr', db.String(16), nullable=False, unique=True)
    txtNome = db.Column('txt_nome_ccr', db.String(100), nullable=False, unique=True)
    txtValidade = db.Column('txt_validade_ccr', db.String(7), nullable=False, unique=True)
    txtCVC = db.Column('txt_cvc_ccr', db.String(3), nullable=False, unique=True)
    datInicio = db.Column('dat_inicio_ccr', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_ccr', db.DateTime, nullable=True)

    user = db.relationship("User")

    def __init__(self, idUsuario, txtNumero, txtNome, txtValidade, txtCVC, datInicio):
        self.idUsuario = idUsuario
        self.txtNumero = txtNumero
        self.txtNome = txtNome
        self.txtValidade = txtValidade
        self.txtCVC = txtCVC
        self.datInicio = datInicio