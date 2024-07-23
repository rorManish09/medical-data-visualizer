import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

height = df['height']

weight = df['weight']
bmi = weight/(height/100)**2

df['overweight'] = (bmi>25).astype(int)

# 3

df['cholesterol'] = (df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)


# 4

def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # 6
    df_cat = df_cat.groupby(by=['cardio','variable','value']).size().reset_index()

    df_cat = df_cat.rename(columns={0:'total'})
    # 7
    bar = sns.catplot(data=df_cat,x='variable',y='total',kind='bar',hue='value',col='cardio')
    # 8
    fig = bar.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo']<=df['ap_hi'])&(df['height']>=df['height'].quantile(0.025))&(df['height']<=df['height'].quantile(.975))&(df['weight']>=df['weight'].quantile(.025))&(df['weight']<=df['weight'].quantile(.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(15,15))

    # 15

    sns.heatmap(corr,mask=mask,square=True,linewidths=.5,annot=True,fmt=".1f")

    # 16
    fig.savefig('heatmap.png')
    return fig
