import configparser
import json
from flask import Flask, render_template
import pymongo 

CONFIG_FILE = "config.ini"
MONGO_URI = "mongodb://localhost:27017/configDB"
DB_NAME = "configDB"
COLLECTION_NAME = "configCollection"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# parse & store config as key value pairs
def parse_config():
  config = configparser.ConfigParser()
  try:
    config.read(CONFIG_FILE)
    if not config.sections():
        raise Exception("Config file is empty.")

    parsed_data = {}

    for section in config.sections():
        parsed_data[section] = {}
        for key, value in config.items(section):
            parsed_data[section][key] = value
    return parsed_data
  except FileNotFoundError:
        print("Error: Configuration file not found.")
        return None
  except Exception as e:
    print(f"Error reading configuration: {e}")
    return None

# Save config to db
def save_config_to_db(data):
    # json_data = json.dumps(data, indent=4)
    existing = collection.find_one(data)
    if existing:
        print("Configuration already exists in DB. Skipping save.")
        return str(existing["_id"])
    result = collection.insert_one(data)
    print("Configuration saved to DB.")
    return str(result.inserted_id)

app = Flask(__name__)
@app.route('/')
# Get config from db
def get_config_from_db():
    data = collection.find()
    return render_template('index.html', data=data)
  
def startup_tasks():
 parsed=parse_config()
 if parsed:
    result=json.dumps(parsed, indent=4)
    print(f"Parsed Configuration:{result}")
    savedId=save_config_to_db(parsed)
    print(f"Saved credentials Id is :{savedId}")

# ---- MAIN SCRIPT ----
if __name__ == '__main__':
    startup_tasks()
    app.run()