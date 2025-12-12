import os
from flask import Flask, redirect, url_for, send_from_directory, render_template


def create_app():
    app = Flask(__name__)

    from . import site
    app.register_blueprint(site.bp, url_prefix='/')


    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('auth/page_not_found.html'), 404

    return app
