from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from api.errors import NoSuchResource, error_index

app = Flask(__name__)
api = Api(app, errors=error_index)

todo_parser = reqparse.RequestParser()


class TodoStorage:

    def __init__(self):
        self.id = 0
        self.items = {}

    def create(self, contents):
        self.id += 1
        contents['id'] = self.id
        self.items[self.id] = contents
        return self.items[self.id]

    def get(self, key):
        return {key: self.items[key]}

    def update(self, key, new):
        item = self.items[key]
        item.update(new)
        self.items[key] = item
        return self.items[key]

    def upsert(self, key, new):
        try:
            return self.update(key, new)
        except KeyError:
            return self.create(new)

    def delete(self, key):
        del self.items[key]

    def serialize(self):
        return list(self.items.values())

todos = TodoStorage()


class Todo(Resource):

    def get(self, todo_id):
        try:
            return todos.get(todo_id)
        except KeyError:
            raise NoSuchResource

    def put(self, todo_id):
        todos.upsert(todo_id, request.get_json())

    def delete(self, todo_id):
        try:
            todos.delete(todo_id)
        except KeyError:
            raise NoSuchResource
        else:
            return None


class TodoList(Resource):

    def get(self):
        return todos.serialize()

    def post(self):
        todos.create(request.get_json())


api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
