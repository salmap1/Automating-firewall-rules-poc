import json
import sys

def validate_rules(file_path):
    with open(file_path, 'r') as file:
        rules = json.load(file)

    for rule in rules:
        if not rule.get("name"):
            print("Validation Error: Rule name missing.")
            sys.exit(1)
        # Add any additional validation checks as needed

validate_rules("security_rules.json")
validate_rules("application_rules.json")

