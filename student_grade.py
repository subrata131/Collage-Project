name=input("Enter Student name:")
marks1=int(input("Enter marks for Subject 1:"))
marks2=int(input("Enter marks for Subject 2:"))
marks3=int(input("Enter marks for Subject 3:"))
total=marks1+marks2+marks3
average=total/3
if average >=90:
  grade='Excellent'

elif average >=75:
  grade='Good'
elif average >=60:
  grade='Average'
elif average >=40:
  grade='Bellow average'
else:
  grade='poor'


n=int(input("Enter Number of Student:"))
for i in range(n):
  print("\nStudent",i+1)

  name=input("Enter Student name:")
  marks1=int(input("Enter marks for Subject 1:"))
  marks2=int(input("Enter marks for Subject 2:"))
  marks3=int(input("Enter marks for Subject 3:"))
  total=marks1+marks2+marks3
  average=total/3
  if average >=90:
    grade='Excellent'

  elif average >=75:
    grade='Good'
  elif average >=60:
   grade='Average'
  elif average >=40:
   grade='Bellow average'
  else:
   grade='poor'

  print("Result:",name, "|Avg:",average, "|Grade:",grade)


  