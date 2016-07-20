import pandas as pd

# from [https://www.kaggle.com/c/titanic/data], [https://www.google.com/url?q=https://www.udacity.com/api/nodes/5420148578/supplemental_media/titanic-datacsv/download&sa=D&ust=1468855513024000&usg=AFQjCNE45kdJmye6jsW73jd-VRNWP3l6Uw]
t_full = pd.read_csv("titanic_data.csv")
#print t.head()
#print t.describe()
t_s = t_full
t_s = t_s.drop("Name",1)
t_s = t_s.drop("PassengerId",1)
t_s = t_s.drop("Ticket",1)
t_s = t_s.drop("Cabin",1)
#print t_s.shape
#t_s.plot.scatter("Pclass", "Fare")
## shows that Class 2 and 3 have similar distributions?

#t_s.boxplot("Fare", "Pclass") 
##yes, indeed distribution very similar. 

#add column "FamSize"
t_s["FamSize"] = t_s["SibSp"] + t_s["Parch"]
#print t_s.shape

#t_s.dropna(axis=0, how='any')
t_s = t_s.dropna()
#print t_s.shape

## export to .csv
#t_s.to_csv("titanic_data_processed_1607191659.csv")