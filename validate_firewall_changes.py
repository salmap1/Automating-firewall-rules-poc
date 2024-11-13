import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_security_rules(file_path):
    try:
        data = load_json(file_path)
        errors = []

        # Example validations:
        for rule in data.get("rules", []):
            if "name" not in rule or not rule["name"].startswith("SEC"):
                errors.append(f"Rule '{rule.get('name', 'unknown')}' does not meet naming convention.")

            if "source" not in rule or not rule["source"]:
                errors.append(f"Rule '{rule['name']}' is missing source.")

        if errors:
            print("Validation Errors:")
            for error in errors:
                print(f" - {error}")
            sys.exit(1)  # Exit with error status if validation fails

        print(f"Validation passed for {file_path}.")
        
    except Exception as e:
        print(f"Error validating {file_path}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to security_rules.json")
        sys.exit(1)

    file_path = sys.argv[1]
    validate_security_rules(file_path)

