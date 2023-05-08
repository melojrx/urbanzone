from flask import Blueprint

compra_bp = Blueprint('compra', __name__)

from ..controller.compraController import *