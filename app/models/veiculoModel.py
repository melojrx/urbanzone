from ..database import db
from app.models.marcaModel import Marca

class Veiculo(db.Model):
    __tablename__ = 'tb_veiculo_vei'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_veiculo_vei', db.Integer, autoincrement=True, primary_key=True)
    idMarca = db.Column('id_marca_vei', db.Integer, db.ForeignKey(Marca.id), nullable=False)
    txtVeiculo = db.Column('txt_veiculo_vei', db.String(200), nullable=False, unique=True)
    imgVeiculo = db.Column('img_veiculo_vei', db.LargeBinary, nullable=False)
    datInicio = db.Column('dat_inicio_vei', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_vei', db.DateTime, nullable=True)

    marca = db.relationship("Marca")