from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app
from api.config import Config
from api.models.base import db

# sets up the app
app = create_app(Config)
manager = Manager(app)
migrate = Migrate(app, db)

# adds the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    manager.run()
