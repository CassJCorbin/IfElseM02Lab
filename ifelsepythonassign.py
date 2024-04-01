
#Assignment: M02 Lab - Case Study: if...else and while
#Name: Cassandra Corbin
#Date: April 1, 2024


while True: #Begin while loop
    last_name = input("Enter the student\'s last name:")  #Have user enter their last name
    if last_name == "zzz":   #If user enters zzz, end program
        break

    first_name = input("Enter the student's first name: ")  #Have user enter their first name
    gpa = float(input("Enter the student's GPA: "))    #Have the user enter their gpa as a float
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")      #If the user enters a number equal or greater than 3.5, they made the deans list.
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")       #If the user enters a number equal or greater than 3.25, they made honor roll.
    elif gpa <3.25:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")    #If the user enters a number less than 3.25, they did not make either.