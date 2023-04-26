import datetime
from ..database import db
from operator import and_
from ..rotas.publicRout import public_bp
from flask import flash, render_template, request, redirect, url_for

class publicController:

        @public_bp.route('/')
        def home():
                return render_template('index.html')


