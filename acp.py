import pandas as pd

data_set={"ID": [1,2,3,4], "Name": ["Pankaj","Meghna",'David','Lisa'], "Role": ['CEO', None,None,None], "Salary": [100,200,None,None]}

df=pd.DataFrame(data_set)

#print intial 2 and last 2 values from data frame
print(df.head(1)) #returns rows
print(df.tail(2))
#df.loc[index] -> returns index in 2 columns, Id - 1, Name - Pankaj etc

#check total number of null values
print(df.isnull().sum())   

# detailed info
print(df.info())

#dropp all row with null and store into new data frame
print(df.dropna())

#drop all colums with null and store new data
print(df.dropna(axis=1))

#Fill null values of Salary with 300
print(df['Salary'].fillna(300,inplace=True))


#Fill null of Role with value CEO
df['Role'].fillna('CEO', inplace=True)
print(df.to_string()) #other way to print using to_string

