import json
import sys
import os

def validate_rules(file_path):
    with open(file_path, 'r') as file:
        rules = json.load(file)

    for rule in rules:
        if not rule.get("name"):
            print("Validation Error: Rule name missing.")
            sys.exit(1)
        # Add additional validation checks here if necessary

# Use relative paths to the IP team directory
validate_rules("teams/ip/security_rules.json")
validate_rules("teams/ip/application_rules.json")

