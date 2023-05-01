from flask import Blueprint

usuarioVeiculo_bp = Blueprint('usuarioVeiculo', __name__)

from ..controller.usuarioVeiucloController import *