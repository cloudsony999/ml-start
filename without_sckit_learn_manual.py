study_hours=[1,2,3,4,5,6,7,8]
marks=[30,35,45,50,60,70,80,90]

n=len(study_hours)

mean_x=sum(study_hours)/n
mean_y=sum(marks)/n

numerator=0
denominator=0

for i in range(n):
    numerator += (study_hours[i]-mean_x)*(marks[i]-mean_y)
    denominator+=(study_hours[i]-mean_x)**2

slope=numerator/denominator
intercept=mean_y-slope *mean_x

print('learned slope ',slope)
print('Learning intercept ',intercept)

new_hours=6

predict_marks=slope*new_hours+intercept

print('Predicted marks: ',predict_marks)




