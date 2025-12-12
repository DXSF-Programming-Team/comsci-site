from flask import Blueprint, render_template, request, redirect, url_for
#from .db import db
from datetime import datetime

'''
class Puzzle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    statement = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    
    # 0 = easy, 1 = medium, 2 = hard
    difficulty = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
'''



bp = Blueprint('puzzles', __name__)


@bp.route('/')
def home():
    return render_template('puzzles/home.html')

@bp.route('/create')
def create():
    return render_template('puzzles/submit_puzzle.html')

@bp.route('/index')
def index():
    return render_template('puzzles/index.html')