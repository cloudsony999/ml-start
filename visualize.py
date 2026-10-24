import pandas as pd
import matplotlib.pylab as plt
data={
    "study_hours":[1,2,3,4,5,6,7,8],
    "marks":[30,35,45,50,60,70,80,90]
}

df=pd.DataFrame(data)

plt.scatter(df['study_hours'],df["marks"])

plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours VS marks')

plt.show()



