import configparser
import json
import os
from flask import Flask, jsonify

# Initialize Flask web app
app = Flask(__name__)

def parse_config(file_path):
    """
    Parse an INI-style configuration file into a dictionary.
    Example structure:
      {
        "Database": {"host": "localhost", "port": "3306", ...},
        "Server": {"address": "192.168.0.1", "port": "8080"}
      }
    """
    config = configparser.ConfigParser()

    # Handle missing file gracefully
    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found!")

    # Read and parse file
    config.read(file_path)
    data = {}

    # Extract section and key-value pairs
    for section in config.sections():
        data[section] = dict(config.items(section))

    return data


def save_to_json(data, json_path="config_data.json"):
    """
    Save parsed configuration data to a JSON file (simulating database storage).
    """
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)


@app.route('/get_config', methods=['GET'])
def get_config():
    """
    REST API endpoint to return stored configuration data as JSON.
    """
    try:
        with open("config_data.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Configuration data not found"}), 404


if __name__ == "__main__":
    try:
        # Specify configuration file
        file_path = "config.ini"

        # Parse and display results
        parsed_data = parse_config(file_path)
        print("✅ Configuration File Parser Results:")
        for section, values in parsed_data.items():
            print(f"{section}:")
            for key, val in values.items():
                print(f" - {key}: {val}")

        # Save parsed data as JSON
        save_to_json(parsed_data)
        print("\n💾 Data saved as config_data.json")

        # Start Flask server to provide GET API
        print("\n🚀 Starting Flask API at http://127.0.0.1:5000/get_config")
        app.run(debug=True)

    except Exception as e:
        print(f"❌ Error: {e}")
