from ..database import db
from flask_login import UserMixin

class CartaoCredito(db.Model, UserMixin):
    __tablename__ = 'tb_estacionamento_est'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_estacionamento_est', db.Integer, autoincrement=True, primary_key=True)
    datInicio = db.Column('dat_inicio_est', db.DateTime, nullable=False)   