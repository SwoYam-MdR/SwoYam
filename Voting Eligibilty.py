print("What is your age")
age=int(input())
if age>18:
    print("You can vote")
elif age==18:
    print("You need to complete some process then you can vote") # Extra step made by me
else:
    print("You cannot vote")
