from flask import Flask, jsonify, request

#my global variable
todos = [{ "label": "My first task", "done": False},
         { "label": "My second task", "done": False},
         { "label": "My third task", "done": False}]

app = Flask(__name__)

#GET
@app.route('/todos', methods=['GET'])
def get_all_todos():
    return todos;

#POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

# request.get_json(force=True)?

#DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("this is the position to delete", position)
    todos.remove(todos[position])
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
