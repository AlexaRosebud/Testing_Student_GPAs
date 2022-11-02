#Alexa Scott
#Testing_Student_GPA's
#My app will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
#Ask for student's last name.
lastName = input("Enter last name: ")
#Check if last name was entered as 'ZZZ' if true quit processing.
while lastName != "ZZZ":
    #Ask user to enter their first name.
    firstName = input("Enter first name: ")
    #Ask user to input their GPA.
    gpa = float(input("Enter GPA: "))
    #Test if student GPA is 3.5 or greater, if so they have made the Dean's List.
    if gpa >=3.5:
        print("{} {} has made the Dean's List.".format(firstName, lastName))
    #Test if student GPA is 3.25 or greater, if so they have made Honor Roll.
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstName, lastName))
    lastName = input("\nEnter last name: ")
#Quit processing student records if the last name entered is 'ZZZ'.