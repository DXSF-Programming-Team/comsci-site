from flask import Blueprint, render_template, send_from_directory
import os

bp = Blueprint('site', __name__)

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(bp.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@bp.errorhandler(404)
def page_not_found(error):
    return render_template('site/page_not_found.html'), 404

@bp.route('/')
def index():
    return render_template('site/homepage.html')


@bp.route('/about')
def about():
    return render_template('site/about.html')

@bp.route('/projects')
def projects():
    return render_template('site/projects.html')

@bp.route('/resources')
def resources():
    return render_template('site/resources.html')