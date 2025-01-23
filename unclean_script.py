import pandas as pd
import numpy as np

def unclean_data(df, int_cols=None, float_cols=None, string_cols=None):
    if int_cols is None:
        int_cols = df.select_dtypes(include='int').columns
    if float_cols is None:
        float_cols = df.select_dtypes(include='float').columns
    if string_cols is None:
        string_cols = df.select_dtypes(include='object').columns

    for col in int_cols:
        df.loc[df.sample(frac=0.05).index, col] = np.nan
    
    for col in float_cols:
        df.loc[df.sample(frac=0.05).index, col] = np.nan

    for col in float_cols:
        outlier_values = df[col].mean() * np.random.uniform(5, 10, size=5)
        outlier_indices = df.sample(n=5).index
        df.loc[outlier_indices, col] = outlier_values

    for col in string_cols:
        sample_idx = df.sample(frac=0.1).index
        df.loc[sample_idx, col] = df.loc[sample_idx, col].apply(
            lambda x: ''.join(np.random.choice([ch.upper(), ch.lower()]) for ch in str(x)) if isinstance(x, str) else x
        )

    for col in string_cols:
        sample_idx = df.sample(frac=0.05).index
        df.loc[sample_idx, col] = df.loc[sample_idx, col].apply(lambda x: f"  {x}  " if isinstance(x, str) else x)

    return df


df = pd.read_csv('crop_yield.csv') 
df_uncleaned = unclean_data(df)
df_uncleaned.to_csv('uncleaned_crop_yield.csv', index=False)