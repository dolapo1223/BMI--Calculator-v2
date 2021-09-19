# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / int(height**2)
bmi_as_whole = int(bmi)

#print(type(bmi))
print("\n=============================================\n")
if bmi <= 18.5:
  print(f"Your bmi is {bmi_as_whole},you are underweight")
elif bmi > 18.5 and bmi <= 25:
  print(f"Your bmi is {bmi_as_whole}, you have a normal weight")
elif bmi > 25 and bmi <= 30:
  print(f"Your bmi is {bmi_as_whole}, You are slightly overweight")
elif bmi > 30 and bmi <= 35:
  print(f"Your bmi is {bmi_as_whole},You are obese")
else:
  print(f"Your bmi is {bmi_as_whole},you are clinically obese")







