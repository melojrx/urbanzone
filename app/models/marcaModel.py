from ..database import db

class Marca(db.Model):
    __tablename__ = 'tb_marca_mar'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_marca_mar', db.Integer, autoincrement=True, primary_key=True)
    txtMarca = db.Column('txt_marca_mar', db.String(200), nullable=False, unique=True)
    txtAbreviacao = db.Column('txt_abreviacao_marca_mar', db.String(10), unique=True)
    imgMarca = db.Column('img_marca_mar', db.LargeBinary, nullable=False)
    datInicio = db.Column('dat_inicio_mar', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_mar', db.DateTime, nullable=True)