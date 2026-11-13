from flask import Flask, render_template, request, redirect, url_for, jsonify
from data_handler import load_items, save_items

app = Flask(__name__)

# بارگذاری آیتم‌ها در حافظه
items = load_items()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/items")
def get_items():
    return render_template("items.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        new_item = {"id": items[-1]["id"] + 1 if items else 1, "name": name, "description": description}
        items.append(new_item)
        save_items(items)
        return redirect(url_for("get_items"))
    return render_template("form.html", action="add")

@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return "Item not found", 404
    if request.method == "POST":
        item["name"] = request.form["name"]
        item["description"] = request.form["description"]
        save_items(items)
        return redirect(url_for("get_items"))
    return render_template("form.html", action="edit", item=item)

@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    save_items(items)
    return redirect(url_for("get_items"))

if __name__ == "__main__":
    app.run(debug=True)
