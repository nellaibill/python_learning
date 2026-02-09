# I want to use os module to read the content of requirements.txt file and display it on the webpage

from flask import  jsonify, redirect, render_template, request, session, url_for,Blueprint
import json
import os
learnings_bp = Blueprint('learnings', __name__)

@learnings_bp.route('/requirements')
def requirements():
    file_path = 'requirements.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return f"<pre>{content}</pre>"
    else:
        return "requirements.txt file does not exist."

@learnings_bp.route('/api/data', methods=['get'])
def api_data():
    #How to return multiple data
 
    data = [{
        "name": "Saleem",
        "age": 35,
        "city": "Karachi"
    },
    {
        "name": "Ali",
        "age": 30,
        "city": "Lahore"
    }]
    
    return jsonify(data)
# How to use json module to read data from a json file and return it as a response
@learnings_bp.route('/api/jsondata')
def json_data():
    file_path = 'data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return "data.json file does not exist."

# I want to write to the json file using json module
@learnings_bp.route('/api/adddata', methods=['POST'])
def add_data():
    new_data = request.get_json()
    file_path = 'data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []
    
    
    data.append(new_data) 
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    return jsonify({"message": "Data added successfully!"})