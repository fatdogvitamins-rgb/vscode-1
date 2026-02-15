import json
readit = open('.jres', 'r')
data = json.load(readit)
print(json.dumps(data, indent=4))