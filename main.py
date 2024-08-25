from flask import Flask, request, jsonify

# Initialize the Flask application
apps = Flask(__name__)

# Home route
@apps.route("/")
def home():
    return "Welcome to our API"

# GET endpoint
@apps.route("/api/get_example", methods=["GET"])
def get_example():
    data = {
        "Message": "This is a GET request",
        "Status": "Success"
    }
    return data

# POST endpoint
@apps.route("/api/post_example", methods=["POST"])
def post_example():
    received_data = request.get_json()
    response = {
        "Status": "Success",
        "Data_received": received_data
    }
    return jsonify(response)

# Entry point to run the application
if __name__ == '__main__':
    apps.run(debug=True)
