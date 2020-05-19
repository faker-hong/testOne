import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
            'female': [0, 1, 1, 0, 1],
            'age': [42, 52, 36, 24, 73],
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns=raw_data.keys())

# preTestScore 和 postTestScore关系的散点图，点的大小由age决定
# plt.scatter(df.preTestScore, df.postTestScore, s=df.age)
# plt.xlabel('preTestScore')
# plt.ylabel('postTestScore')
# plt.title("preTestScore x postTestScore")
# plt.show()


# preTestScore 和 postTestScore关系的散点图,颜色由female决定，大小为postTestScore的4倍
plt.scatter(df.preTestScore, df.postTestScore, s=df.postTestScore*4, c=df.female)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title("preTestScore x postTestScore")
plt.show()