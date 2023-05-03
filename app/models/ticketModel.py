from ..database import db
from flask_login import UserMixin

class Ticket(db.Model, UserMixin):
    __tablename__ = 'tb_ticket_tic'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_ticket_tic', db.Integer, autoincrement=True, primary_key=True)
    txtTicket = db.Column('txt_descricao_tic', db.String(100), nullable=False, unique=True)
    valorTicket = db.Column('num+valor_tic', db.Double, nullable=False)
    horaTicket = db.Column('num_horas_tic', db.Smallint, nullable=False)
    datInicio = db.Column('dat_inicio_tic', db.DateTime, nullable=False)
    datFim = db.Column('dat_fim_tic', db.DateTime, nullable=True)