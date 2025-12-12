import os
from flask import Flask, redirect, url_for, send_from_directory, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )


    from . import site
    app.register_blueprint(site.bp, url_prefix='/')

    from . import puzzles
    app.register_blueprint(puzzles.bp, url_prefix='/puzzles')
    app.add_url_rule('/puzzles', endpoint='puzzles.home')

    from . import db
    db.init_app(app)


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
