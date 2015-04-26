import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#plotting the Plotbox
loansData.boxplot(column="Amount.Requested")
plt.show()
'''the plot box shows for "Amount.Requested" compared with the plotbox created from the column 'Amount.Funded.By.Investors' shows that the amount requested has a similar distribution to the amount funded and its around the $1000 dollar value""#
Histogram'''
loansData.hist(column='Amount.Requested')
plt.show()
''' the histogram shows that the amount requested buy the creditees lays btween the $500 and the 1000 dollar mark'''
# plotting QQ-plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
#This graph shows that the distrubution is converged within the 500 and 1000 dollars
