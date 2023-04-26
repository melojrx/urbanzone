from ..database import db
from flask_login import UserMixin

class Veiculo(db.Model, UserMixin):
    __tablename__ = 'tb_veiculo_vei'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_veiculo_vei', db.Integer, autoincrement=True, primary_key=True)
    txtVeiculo = db.Column('txt_veiculo_vei', db.String(200), nullable=False, unique=True)
    txtAbreviacao = db.Column('txt_abreviacao_marca_mar', db.String(10), unique=True)
    imgVeiculo = db.Column('img_veiculo_vei', db.LargeBinary, nullable=False)
    datInicio = db.Column('dat_inicio_vei', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_vei', db.DateTime, nullable=True)