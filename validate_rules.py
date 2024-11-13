import json
import sys
import os

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def detect_changes(old_data, new_data):
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    added = new_keys - old_keys
    deleted = old_keys - new_keys
    modified = {key for key in old_keys & new_keys if old_data[key] != new_data[key]}

    return {
        "added": list(added),
        "deleted": list(deleted),
        "modified": list(modified),
        "added_data": {key:new_data[key] for key in added},
        "modified_data": {key:new_data[key] for key in modified}
    }

def validate_rules(file, team):
    old_file = f"old_{file}"
    new_file = f"new_{file}"

    if os.path.exists(old_file) and os.path.exists(new_file):
        old_data = load_json(old_file)
        new_data = load_json(new_file)
        changes = detect_changes(old_data, new_data)

        errors = []
        if team == "ip":
            # IP team-specific rules
            for added_rule in changes["added"]:
                if not new_data[added_rule].get("name", "").startswith("IP_"):
                    errors.append(f"IP team rule '{added_rule}' does not start with 'IP_'.")

        elif team == "noc":
            # NOC team-specific rules
            for added_rule in changes["added"]:
                if not new_data[added_rule].get("name", "").startswith("NOC_"):
                    errors.append(f"NOC team rule '{added_rule}' does not start with 'NOC_'.")

        # Other team-specific validations

        if errors:
            print("Validation Errors:")
            for error in errors:
                print(f" - {error}")
            sys.exit(1)  # Exit with error status if validation fails

        return changes
    else:
        print(f"Could not find both versions of {file} for comparison.")
        return {}

if __name__ == "__main__":
    # Determine team and file from arguments
    team = sys.argv[1]  # Either 'ip' or 'noc'
    file = sys.argv[2]  # The file to validate
    validate_rules(file, team)

