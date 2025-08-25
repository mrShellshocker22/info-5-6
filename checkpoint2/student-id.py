def main():
    print('')
    print('Please enter the following information to create your ID Card.')
    input('Press enter to continue.')



    Fname = input("Please enter your first name: ")
    Lname = input("Please enter your last name: ")
    email = input("Please enter your email address: ")
    Pnunmber = input("Please enter your phone number: ")
    id_number = input("Please enter your student ID number: ")
    ftp = input("Please enter your FPT Class: ")
    gclass = input("Please enter your graduation class: ")
    favsubject = input("Please enter your favorite subject: ")
    extcurricular = input("Do you participate in any extracurricular activities (yes / no): ")


    print("Your ID Card is:")
    print("---------------------------------------------")
    print(f"{Lname}.upper() ", " {Fname}.capitalize()")
    print(f"ID: {id_number}")
    print("")
    print(f"Email: {email}")
    print(f"Phone: {Pnunmber}")
    print("")
    print(f"FPT Class : {ftp} \t Fav Subject: {favsubject}.capitalize()")
    print(f"Expected Graduation: {gclass} \t Years left: {gclass - 2025}")
    print(f"Extracurricular Activities: {extcurricular}")
    print("---------------------------------------------")