import json
import pprint
str_json = '''
{
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "User ID"
        },
        "first_name": {
          "type": "string",
          "description": "User first name"
        },
        "last_name": {
          "type": "string",
          "description": "User last name"
        }
      },
      "required": [
        "id",
        "first_name",
        "last_name"
      ],
      "additionalProperties": false
}
'''
data = json.loads(str_json)
pprint.pprint(data)
print(data['properties']['id'])
for item in data['required']:
    print(item)
new_json = data
print(json.dumps(new_json, indent=2))

with open('file_json', 'w') as file:
    json.dump(new_json, file, indent=3)
