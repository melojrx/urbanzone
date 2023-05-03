from flask import Blueprint

cartaoCredito_bp = Blueprint('cartaoCredito', __name__)

from ..controller.cartaoCreditoController import *