import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'SF', 'LA']}

df = pd.DataFrame(data)

transposed_df = df.transpose()
transposed_df_alt = df.T
print(transposed_df_alt)