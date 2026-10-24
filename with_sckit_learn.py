import numpy as np
from sklearn.linear_model import LinearRegression

X=np.array(
    [[1],[2],[3],[4],[5],[6],[7],[8]]
)

y=np.array([30,35,45,50,60,70,80,90])

model=LinearRegression()

model.fit(X,y)

print('Coefficient: ',model.coef_[0])
print('Intercept: ',model.intercept_)

new_student=np.array([[6.5]])

prediction=model.predict(new_student)

print('Predicted Marks: ',prediction[0])




