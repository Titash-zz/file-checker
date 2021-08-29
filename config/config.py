import json

config_json = '[{"file_name": "README.md", "expected_time": "13:00"}, {"file_name": "LICENSE", "expected_time": "22:00"}]'

def get_congif():
  return json.loads(config_json)