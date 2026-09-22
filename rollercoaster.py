#program to find if a person can ride a rollercoaster based on height
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the RollerCoaster!")
    age = int(input("What is your age? "))
    if age <= 12 :
        print("Please pay $5 for the ticket.")
    elif age <=18 :
        print("Please pay $7 for the ticket.")    
    else:
        print("Please pay $12 for the ticket.")
else:
    print("Sorry, you need to grow taller to ride the RollerCoaster.")