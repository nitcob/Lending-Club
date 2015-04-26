import matplotlib.pyplot as pl
import pandas as pd
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#Remove the "%" symbol from the interest rate to make it into an integer

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))

#Make the interest rates floats

loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)

#remove string

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()

FICO=[]
for j in range(len(A)):
    B = A[j].split("-")
    C = float(B[0])
    FICO.append(C)
loansData['FICO.Score']=FICO
inrate = loansData["Interest.Rate"]
loanamt = loansData["Amount.Requested"]
fico = loansData["FICO.Score"]

# Convert the lists into numpy vectors
# The dependent variable
y = np.matrix(inrate).transpose()

# First feature
x1 = np.matrix(fico).transpose()

# Second feature
x2 = np.matrix(loanamt).transpose()

# Input matrix of all features
x = np.column_stack([x1, x2])
X = sm.add_constant(x)

# Train the model
model = sm.OLS(y, X)
f = model.fit()

# Print the results
print 'Coefficients: ', f.params
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

# Print the fitted line and the original data for the two features selected
theta = np.matrix(f.params).transpose()
yf_fitted = np.dot(X, theta)
pl.plot(x2, y, 'o', mew=0, mfc="#FF8080", ms=5)
pl.plot(x2, yf_fitted, lw=3)
pl.xlabel("FICO score")
pl.ylabel("Interest rate")
pl.show()
