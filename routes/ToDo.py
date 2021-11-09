from flask_restful import Resource
from flask import request
from models.task import Task
from app import db


class Todo(Resource):

    # route for GET '/todo/<todo_id>'
    def get(self, todo_id):

        todo_id = int(todo_id)
        task = Task.query.get(todo_id)
        if not task:
            return {"error": f"Could not find task {todo_id}"}, 404

        return {
            "todo": {
                "id": task.id,
                "name": task.name,
            }
        }, 200

    # put /todo/<todo_id>
    def put(self, todo_id):
        body = request.get_json()
        print(body)
        task = Task.query.get(todo_id)
        if not task:
            return {"error": f"Could not find task {todo_id}"}, 404

        task.name = body["name"]
        db.session.commit()
        return {
            "todo": {
                "id": task.id,
                "name": task.name,
            }
        }, 200

    def delete(self, todo_id):
        task = Task.query.get(todo_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {"message": f"Task {todo_id} {task.name} DELETED"}, 200

        return {"error": f"Could not find task {todo_id}"}, 404


class TodoList(Resource):
    def get(self):
        tasks = Task.query.all()
        output = []
        for task in tasks:
            output.append(task.to_dict())

        return output, 200

    def post(self):
        body = request.get_json()

        if "name" in body:
            new_task = Task(name=body["name"])
            Task.query.session.add(new_task)
            Task.query.session.commit()
            return new_task.to_dict(), 201
        else:
            return {"error": "name is required"}, 400
