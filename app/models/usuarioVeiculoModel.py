from ..database import db
from flask_login import UserMixin

class CartaoCredito(db.Model, UserMixin):
    __tablename__ = 'tb_usuario_veiculo_uve'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_usuario_veiculo_uve', db.Integer, autoincrement=True, primary_key=True)
    txtPlaca = db.Column('txt_placa_vei', db.String(7), nullable=False, unique=True)
    datInicio = db.Column('dat_inicio_vei', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_vei', db.DateTime, nullable=True)   