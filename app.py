from flask import Flask
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize SQL Alchemy
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    from routes.ToDo import Todo
    from routes.ToDo import TodoList

    app = Flask(__name__)
    api = Api(app)

    # Config App and SQL Alchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    api.add_resource(Todo, '/todo/<string:todo_id>')
    api.add_resource(TodoList, '/todos')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_CONNECTION_STRING')

    # Import Models Here!
    from models.task import Task

    # Hook up Flask & SQL Alchemy
    db.init_app(app)
    migrate.init_app(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
