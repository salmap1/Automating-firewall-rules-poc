import json
import sys
import os

def validate_rules(file_path):
    try:
        with open(file_path, 'r') as file:
            rules = json.load(file)

        for rule in rules:
            if not rule.get("name"):
                print(f"Validation Error in {file_path}: Rule name missing.")
                sys.exit(1)
            # Additional validations can go here

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

# Specify the paths for the IP team validation
validate_rules(os.path.join("teams", "ip", "security_rules.json"))
validate_rules(os.path.join("teams", "ip", "application_rules.json"))

