import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#check columns that need to be cleaned

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

#clean data#
#Remove the "%" symbol from the interest rate to make it into an integer
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
#Make the interest rates floats
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
#remove string
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

#convert the data in FICO.Range into string and split the string and take the lowest value
loansData['FICO.Score'] = loansData['FICO.Range'].astype(str)

loansData['FICO.Score'] = loansData['FICO.Range']
A=loansData['FICO.Score'].tolist()
FICO=[]
for j in range(len(A)):
    B = A[j].split("-")
    C = float(B[0])
    FICO.append(C)

loansData['FICO.Score']=FICO

# logistic regression

intercept = [1] * len(loansData)
loansData['Intercept'] = intercept

# independant variables

ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']
ir = loansData['Interest.Rate']
ir = [1 if x < 12 else 0 for x in ir]
loansData['IR_TF'] = ir
X = loansData[ind_vars]
y = loansData['IR_TF']

logit = sm.Logit(y, X)
result = logit.fit()
coeff = result.params
print coeff
