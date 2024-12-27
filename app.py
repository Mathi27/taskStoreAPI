from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# array to store for tasks
todos = []

@app.route("/")
def home():
    return render_template("todo.html", todos=todos, enumerate=enumerate)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append({"task": task, "done": False})
    return redirect(url_for("home"))

@app.route("/toggle/<int:task_index>")
def toggle(task_index):
    if 0 <= task_index < len(todos):
        todos[task_index]["done"] = not todos[task_index]["done"]
    return redirect(url_for("home"))

@app.route("/delete/<int:task_index>")
def delete(task_index):
    if 0 <= task_index < len(todos):
        todos.pop(task_index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
