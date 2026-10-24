from matplotlib.testing import subprocess_run_for_testing

study_hours=[1,2,3,4,5]

marks=[35,40,45,65,75]

print('study hours: ',study_hours)

print('Student marks: ',marks)

for i in range(len(study_hours)):
    print('Study Hours: ',study_hours[i]," Marks: ",marks[i])
