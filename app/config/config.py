import json

config_json = '[{"file_name": "README.md", "expected_time": "13:00", "isActive": "Y"}, {"file_name": "LICENSE", "expected_time": "22:00", "isActive": "Y"}]'

def get_config():
  return json.loads(config_json)