from flask_restful import Resource
from flask import request


class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: 1}

    def put(self, todo_id):
        body = request.get_json()
        return body
