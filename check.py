# This program checks if a person is eligible to apply for a job based on their age, diploma, and Id.
age = int(input("Enter your age: "))
has_diploma = input("Do you have a diploma? (y/n):").lower()
has_Id = input("Do you have an Id? (y/n):").lower()
# Check eligibility for the job based on age, diploma, and Id
if age >= 18 and has_diploma == 'y' and has_Id == 'y':
    print("You are eligible to apply for the job.")
elif age >= 18 and has_diploma == 'y' and has_Id == 'n':
    print("You need to have an Id to apply for the job.")
elif age >= 18 and has_diploma == 'n' and has_Id == 'y':
    print("You need to have a diploma to apply for the job.")
elif age >= 18 and has_diploma == 'n' and has_Id == 'n':
    print("You need to have both a diploma and an Id to apply for the job.")
elif age < 18 and has_diploma == 'y' and has_Id == 'y': 
    print("You need to be at least 18 years old to apply for the job.")
else:    print("You need to be at least 18 years old and have both a diploma and an Id to apply for the job.")