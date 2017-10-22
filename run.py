import os

from myapp import create_app

basedir = os.path.abspath(os.path.dirname(__file__))

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
