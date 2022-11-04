# -*- coding: utf-8 -*-
"""credit_card_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14FGrBETjiNTo4TCO96Otyxb1rjPPyxFA
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/creditcard.csv')
df.head()

df.shape

df.info()

df.isnull().sum() 
#no missing values

df[df.isnull().any(axis=1)]

#for dropping the Nan values  
#df = df.apply (pd.to_numeric, errors='coerce') #as the nullvalues are smalland datset is very large so we can drpop the missing valuexs 
#df = df.dropna()

df.describe()

import seaborn as sns 
from matplotlib import pyplot as plt
ax=plt.subplots(figsize=(10,10))
sns.distplot(df.Class)

df['Class'].value_counts() # highly imbalanced data o=notrmal, and 1=fraud

import matplotlib.pyplot as plt
plt.pie(df['Class'].value_counts(),labels=[0,1],autopct='%0.2f')
plt.show()

#separating the fraudulent and norm al

normal=df[df.Class==0] # storing the entire rows of legit data into the normal 
fraud=df[df.Class==1]

fraud.shape

normal['Amount'].describe()

fraud['Amount'].describe()

#compare the values for the transactions

df.groupby('Class').mean()

#dealing with this unbalanced data
#under-sampling
#build a sample dataset containing simlar distribution of normal and fraudulent transactions

normal_sample=normal.sample(n=492) 
# getting 492 random samples from normal transactions
#making of new datset

# concatenating the dataframe ,making of new dataset
df1=pd.concat([normal_sample,fraud],axis=0)

df1.shape

df1['Class'].value_counts()

df1.groupby('Class').mean()
#didnt see much changes n

import matplotlib.pyplot as plt
plt.pie(df1['Class'].value_counts(),labels=[0,1],autopct='%0.2f')
plt.show()

x=df1.drop(columns='Class',axis=1)
y=df1['Class']

x.head()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=.2)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()



lr.fit(x_train,y_train)

from sklearn.metrics import accuracy_score

y_pred=lr.predict(x_test)

accuracy_score(y_test, y_pred)

y_train_pred=lr.predict(x_train)

accuracy_score(y_train_pred,y_train)

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#after tuning 
x.head()

y.head()

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(x_train,x_test)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=.2)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

lr.fit(x_train,y_train)

y_pred2=lr.predict(x_test)

accuracy_score(y_test, y_pred2)

y_train_pred2=lr.predict(x_train)

accuracy_score(y_train_pred2,y_train)

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred2))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred2)))