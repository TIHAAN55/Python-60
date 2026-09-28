print("=== Swimming pool entry center ===")
print("Answer 3 simple questions and I will tell you which pool you can use. \n")

age = int(input("What is your age?"))

if age <= 13:
    print("Your age group is 1-13")
else: 
    print("Your age group is 14-17")
    
level = input("Are you new to swimming?")

if level == "yes":
    print("Your pool will be shallow")
elif level == "no":
    print("Your pool will be deep")
    
phobiaish = input("Are you hydrophobic?")

if phobiaish == "yes":
    print("Your pool will be shallow")
else: 
    print("Your pool will be deep")