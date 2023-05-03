from app.models.veiculoModel import Veiculo
from app.models.userModel import User
from ..database import db

class UsuarioVeiculo(db.Model):
    __tablename__ = 'tb_usuario_veiculo_uve'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_usuario_veiculo_uve', db.Integer, autoincrement=True, primary_key=True)
    idUsuario = db.Column('id_usuario_uve', db.Integer, db.ForeignKey(User.id), nullable=False)
    idVeiculo = db.Column('id_veiculo_uve', db.Integer, db.ForeignKey(Veiculo.id), nullable=False)
    txtPlaca = db.Column('txt_placa_uve', db.String(7), nullable=False, unique=True)
    datInicio = db.Column('dat_inicio_uve', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_uve', db.DateTime, nullable=True)   

    user = db.relationship("User")
    veiculo = db.relationship("Veiculo")

    def __init__(self, idUsuario, idVeiculo, txtPlaca, datInicio):
        self.idUsuario = idUsuario
        self.idVeiculo = idVeiculo
        self.txtPlaca = txtPlaca
        self.datInicio = datInicio