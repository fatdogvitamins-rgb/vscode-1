import json
import pandas as pd
readit = open('.jres', 'r')
data = json.load(readit)
print(json.dumps(data, indent=int('4'), ensure_ascii=False))
df = pd.DataFrame({
    "sonic": {
        ".": {
            "": None,
            "blue": True
        }
    }
})
[print(df.sonic.to_string(buf=None,max_rows=None)) for _ in range(3)]