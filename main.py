from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder=".")

tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Make a list example", "completed": False},
    {"id": 3, "title": "Write code", "completed": False},
    {"id": 4, "title": "Complete your works", "completed": False}
]


@app.route("/")
def home():
    return render_template("gorev.html", tasks=tasks)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return render_template("gorev.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    completed = request.form.get("completed") == "true"  # Doğru kontrol
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": completed
    }
    tasks.append(new_task)
    # JSON yanıt
    return jsonify({"message": "Task added successfully!", "task": new_task})


@app.route("/update_tasks", methods=["POST"])
def update_tasks():
    # İşaretlenen görevlerin ID'lerini al
    completed_tasks = request.form.getlist("completed_tasks")

    # Görevleri güncelle
    for task in tasks:
        task["completed"] = str(task["id"]) in completed_tasks  # ID eşleşirse true yap

    # Görev listesini tekrar göster
    return render_template("gorev.html", tasks=tasks)


# Show All tasks route
@app.route("/show_tasks", methods=["GET"])
def show_tasks():
    print("SHOWING ALL TASKS")
    # Pass the list of users to the template
    return render_template("template.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug="True")
