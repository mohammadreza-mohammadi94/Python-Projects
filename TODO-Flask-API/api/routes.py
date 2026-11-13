from flask import Blueprint, jsonify, request

todo_api = Blueprint("todo_api", __name__)

# Initial Data in TODO
items = [
    {'id': 1, 'name': "Item 1", 'description': "This is item 1"},
    {'id': 2, 'name': "Item 2", 'description': "This is item 2"}
]

@todo_api.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@todo_api.route("/items/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    return jsonify(item) if item else jsonify({"Error": "Item Not Found."}), 404

@todo_api.route("/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"Error": "Invalid Request."}), 400
    
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

@todo_api.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error": "Item Not Found."}), 404

    item["name"] = request.json.get('name', item['name'])
    item["description"] = request.json.get('description', item['description'])
    return jsonify(item)

@todo_api.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"Result": "Item Deleted"}), 200
