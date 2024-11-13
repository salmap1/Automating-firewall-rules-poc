import json
import sys

def validate_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        return True, json_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {file_path}: {e}")
        return False, None

if __name__ == "__main__":
    valid_app, app_data = validate_json('application.json')
    valid_sec, sec_data = validate_json('security.json')

    if not valid_app or not valid_sec:
        print("Invalid JSON detected. Please check your changes.")
        sys.exit(1)

    # Additional validation logic for rule compliance can be added here
    print("Validation successful.")

