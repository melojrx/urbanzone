from flask import Blueprint

estacionamento_bp = Blueprint('estacionamento', __name__)

from ..controller.estacionamentoController import *