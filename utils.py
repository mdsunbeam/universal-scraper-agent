import json

# Function to load JSON file as dictionary
def load_json_as_dict(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json_to_file(json_object, filename):
    try:
        with open(filename, 'w') as json_file:
            json.dump(json_object, json_file, indent=4)
        print(f"JSON data has been successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving JSON to file: {e}")