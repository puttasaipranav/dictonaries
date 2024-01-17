import pandas as pd

df = pd.read_csv('your_file.csv',delimiter='|')
null_values = df['family_cfr'].isnull()
print(df[null_values])