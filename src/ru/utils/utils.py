import pandas as pd

file = '../verbalizer/cardinals.tsv'

df = pd.read_csv(file, header=None, sep='\t', names=['num', 'words'])
print(df.head())

def clean(text):
    text = text.replace('ё', 'e')
    # replace Eng 'e' to Ru
    text = text.replace('e', 'е').replace("e", "е")
    return text

df['words'] = df['words'].apply(lambda x: clean(x))
print(df.head())
df.to_csv(file, header=None, sep='\t', index=None)