import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df_nat = pd.read_csv('mx.csv')

df_nat.date = pd.to_datetime(df_nat.date)
df_nat.cases = pd.to_numeric(df_nat.cases)
df_nat['new_cases'] = df_nat.cases.diff()
df_nat['growth_new_cases'] = df_nat.new_cases.diff()

sns.set(rc={'figure.figsize':(11.7,6.27)})
sns.lineplot(
    x = 'date',
    y ='new_cases',
    data = df_nat)

plt.show()