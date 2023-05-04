from app.models.usuarioVeiculoModel import UsuarioVeiculo
from app.models.compraModel import Compra
from ..database import db

class Estacionamento(db.Model):
    __tablename__ = 'tb_estacionamento_est'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_estacionamento_est', db.Integer, autoincrement=True, primary_key=True)
    idUsuarioVeiculo = db.Column('id_usuario_veiculo_est', db.Integer, db.ForeignKey(UsuarioVeiculo.id), nullable=False)
    idCompra = db.Column('id_compra_est', db.Integer, db.ForeignKey(Compra.id), nullable=False)
    datInicio = db.Column('dat_inicio_est', db.DateTime, nullable=False)   

    usuarioVeiculo = db.relationship("UsuarioVeiculo")
    compra = db.relationship("Compra")

    def __init__(self, idUsuarioVeiculo, compra, datInicio):
        self.idUsuarioVeiculo = idUsuarioVeiculo
        self.compra = compra
        self.datInicio = datInicio