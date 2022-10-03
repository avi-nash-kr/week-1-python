

import json
import pandas as pd

a=pd.read_json("jsonfile.js")
b=pd.DataFrame(a)
print(b)
