from ..database import db
from flask_login import UserMixin

class Compra(db.Model, UserMixin):
    __tablename__ = 'tb_compra_com'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_compra_com', db.Integer, autoincrement=True, primary_key=True)
    qtdCartao = db.Column('qtd_cartao_com', db.Smallint, nullable=False)
    datInicio = db.Column('dat_inicio_sdo', db.DateTime, nullable=False)