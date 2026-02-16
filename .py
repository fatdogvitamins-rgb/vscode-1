import json
import pandas as pd
readit = open('.jres', 'r')
data = json.load(readit)
print(json.dumps(data, indent=int('4'), ensure_ascii=False))