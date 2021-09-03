from sklearn import linear_model
import numpy as np
import pandas
import pandas as pd

df = pandas.read_csv('data.csv')
date = pandas.read_csv('date.csv')

#print(df[['Date']])>

#According to Range and Fully Loaded
X = date.iloc[:,0:1]

#Base Price
y = df.drop(['Date'],axis = 'columns')

regresyon = linear_model.LinearRegression()

regresyon.fit(X, y)

print(""" Number 59 marks September 2, 2021. Number 89 marks October 2, 2021.
          You can guess between 60 and 89.

""")

#aaa = " ," * 59
#print("a",aaa,"a")

#for x in range(60,90):
    #predicted_date = regresyon.predict([[x]])
    #a = numpy.array(predicted_date)
    #b = a.tolist()

model_ml = linear_model.LinearRegression()
model_ml.fit(X, y)
date_enter = int(input("Date enter: (Example: 60 = 03 SEPTEMBER 2021): "))


try:
    while True:
        predicted_date = model_ml.predict([[date_enter]])
        toarray = np.array(predicted_date)
        tolist = toarray.tolist()
        #print(tolist)
        date_predict = pd.read_csv('date_predict.csv',index_col=None, na_values=None)
        date_detect_algorithm = date_predict.columns[date_enter]
        for x in tolist:
            print("""Predicted Date: {},\nPrediction Number of Cases Today: {},\nNumber of Tests Today: {},\nNumber of Deaths Today: {},\nNumber of Healing Today: {}""".format(date_detect_algorithm, int(x[0]),int(x[1]),int(x[2]),int(x[3])))
        break
except:
    print("Repeat Try :))")
