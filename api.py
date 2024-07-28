import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to genocidal regime!'

@app.route('/login', methods=['POST'])
def post_data():
    data = request.get_json()  # Assuming JSON data
    # Process the data here
    result = process_data(data)  # Example function
    return jsonify(result)

def process_data(data):
  user_name = data["name"]
  assassin_list = load_json_data("assassin_list.json")

  # Check if user name exists in the assassin list
  accepted = user_name.lower() in [name.lower() for name in assassin_list]

  # Update return value with accepted flag
  return {'message': 'Data received successfully', 'accepted': accepted}

def load_json_data(path):
  with open(path, 'r') as f:
    data = json.load(f)
  return data

if __name__ == '__main__':
    app.run(debug=True)
