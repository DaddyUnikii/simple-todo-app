from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Data dummy to-do list
todos = [
    {"id": 1, "task": "Belajar Rust", "done": False},
    {"id": 2, "task": "Baca buku", "done": True}
]
next_id = 3

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.json
    todo = {"id": next_id, "task": data["task"], "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo)

@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    for todo in todos:
        if todo["id"] == id:
            todo["done"] = not todo["done"]
            return jsonify(todo)
    return jsonify({"error": "Todo tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)
