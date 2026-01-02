height =float(input("Enter your height in(cm):"))
weight =float(input("Enter your weight in(kg):"))

BMI = weight / (height/100)**2
print ("Your BMI is:", BMI)

if BMI<= 18.4:
 print("Your underweight")
elif BMI<= 24.9:
  print("Your healthy")
elif BMI<= 29.9:
  print("Your overweight")

elif BMI<= 34.9:
  print("Your severely overweight")

elif BMI<= 39.9:
  print("Your obese")

else:
   print("Your severely obese")

