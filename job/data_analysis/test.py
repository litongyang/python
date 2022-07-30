import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 20, (3, 2)), columns=['A', 'B'])
print(df)

narry = np.random.randint(0, 20, (2, 2))
data = pd.DataFrame(narry, columns=['A', 'B'])
print(data)
print(df.append(data, ignore_index=True))