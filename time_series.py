import pandas as pd
import numpy as np
import statsmodels
from os.path import join
import matplotlib.pyplot as plt
import statsmodels.api as sm

df= pd.read_csv('LoanStats3b.csv', header= 1, low_memory= False)
df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) # converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
plt.plot(loan_count_summary)
plt.show()

''' The breackout points on the graph seem to be to abrupt this might be because there is not enough data
on the dataset to smooth the graph down and eliminate volatilty.'''

fig_1 = sm.graphics.tsa.plot_acf(df['loan_amnt'])
plt.show()
fig_2 = sm.graphics.tsa.plot_pacf(df['loan_amnt'])
plt.show()
