from ..models.cartaoCreditoModel import CartaoCredito
from ..models.ticketModel import Ticket
from ..database import db

class Compra(db.Model):
    __tablename__ = 'tb_compra_com'
    __table_args__ = {"schema":"zone"}

    id = db.Column('id_compra_com', db.Integer, autoincrement=True, primary_key=True)
    idCartaoCredito = db.Column('id_cartao_credito_com', db.Integer, db.ForeignKey(CartaoCredito.id), nullable=False)
    idTicket = db.Column('id_ticket_com', db.Integer, db.ForeignKey(Ticket.id), nullable=False)
    qtdCartao = db.Column('qtd_cartao_com', db.SmallInteger, nullable=False)
    datInicio = db.Column('dat_inicio_sdo', db.DateTime, nullable=False)

    cartaoCredito = db.relationship("CartaoCredito")
    ticket = db.relationship("Ticket")

    def __init__(self, idCartaoCredito, idTicket, qtdCartao, datInicio):
        self.idCartaoCredito = idCartaoCredito
        self.idTicket = idTicket
        self.qtdCartao = qtdCartao
        self.datInicio = datInicio