from flask import Blueprint

usuarioVeiculo_bp = Blueprint('usuarioveiculo', __name__)

from ..controller.usuarioVeiucloController import *