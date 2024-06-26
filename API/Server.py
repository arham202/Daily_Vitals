from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Store the extracted numbers globally
extracted_numbers = []

@app.route('/api/blood_sugar', methods=['POST'])
def receive_blood_sugar_data():
    """Endpoint to receive blood sugar data."""
    global extracted_numbers
    try:
        data = request.get_json()
        print("Received blood sugar data:", data)  # Print the received data
        
        # Extract all numbers from the received data
        numbers = re.findall(r'\d+(?:\.\d+)?', str(data))
        print("Extracted numbers:", numbers)
        
        # Store the extracted numbers globally
        extracted_numbers = numbers

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        print("Error receiving blood sugar data:", e)
        return jsonify({"error": "Failed to process request"}), 500

@app.route('/api/get_data_sugar', methods=['POST'])
def get_data_sugar():
    """Endpoint to handle the request for sending data."""
    global extracted_numbers
    try:
        # Create the response JSON with Q1 as extracted numbers and Q2 as "always"
        response_data = {
            'Q1': extracted_numbers,
            'Q2': 'after'
        }
        print("Data being sent:", response_data)  # Print the data being sent

        # Send the response JSON
        return jsonify(response_data), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify({"error": "Failed to process request"}), 500

@app.route('/api/insulin_taken', methods=['POST'])
def receive_insulin_data():
    """Endpoint to receive insulin data."""
    try:
        data = request.get_json()
        print("Received insulin data:", data)  # Print the received data
        
        # Process the received data as needed

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        print("Error receiving insulin data:", e)
        return jsonify({"error": "Failed to process request"}), 500
@app.route('/api/submit_data_sugar', methods=['POST'])
def submit_data_sugar():
    """Endpoint to receive submitted sugar data."""
    try:
        data = request.get_json()
        print("Received submitted sugar data:", data)  # Print the received data
        
        # Process the received data as needed

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        print("Error receiving submitted sugar data:", e)
        return jsonify({"error": "Failed to process request"}), 500


if __name__ == '__main__':
    app.run(debug=True)