import pandas as pd

data={
    "study_hours":[1,2,3,4,5,6,7,8],
    "attendance":[50,55,60,65,70,75,80,90],
    "marks":[30,35,45,50,60,70,80,90]
}

df=pd.DataFrame(data)

print('Complete DataSet: ')
print(df)

print(df.head())

# print(df.info())

print(df.describe())

