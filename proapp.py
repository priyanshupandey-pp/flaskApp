from flask import Flask,jsonify,request

app = Flask(__name__)

#creating an array of contacts with each task as a different object in it
tasks = [
    {
        'id' : 1,
        'title' : u'buy groceries',
        'description' :u'milk,cheese,curd,fruit',
        'done' : False
    },
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    
if __name__ == "__main__":
    app.run()