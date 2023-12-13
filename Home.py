from Relation import Doctors
from Diseases_with_Doctors import Dict

def view_diseases_and_doctors():
    print("\nList of Diseases:")
    for disease in Dict:
        print(disease)
        

    print("\nList of Doctors:")
    for doctor in Dict.values():
        print(doctor)

def prompt_user_for_disease():
    print("\nDisease and Doctor Assignment:")
    while True:
        try:
            patient = input("Enter your name: ")
            disease = input("Enter the disease you are suffering from: ")
        except Exception:
            print("Error!")
        else:
            if disease in Dict:
                print("A doctor will be assigned to you in a minute.")
                assigned_doctor = Dict[disease]
                print(f"Your doctor is: {assigned_doctor} => a specialist in {disease}")
                break
            else:
                print(f"We do not treat {disease} at the moment.")
        finally:
            print("\nLETS FIGHT DISEASES TOGETHER")

if __name__ == "__main__":
    # Logging in to the system or creating an account
    while True:
        user_input = input("\nAre you an existing user? (yes/no): ").lower()
        
        if user_input == "yes":
            user_name = input("Enter User Name: ")
            password = int(input("Enter Password: "))  # Password should be hashed in a real-world scenario

            # Implement your login logic here
            # For simplicity, let's assume a hardcoded username and password
            if user_name == "Robinson" and password == 2030:
                print("Successfully Logged in.")
                break
            else:
                print("Incorrect username and password. Please try again.")
        elif user_input == "no":
            print("\nCreate an account:")
            user_name = input("\nEnter User Name: ")
            create_password = int(input("Enter Password: "))
            repeat_password = int(input("Confirm Password: "))
           
            if create_password != repeat_password:
                print("Password does not match. Please try again.")
            else:
                print(".....verifying.....")
                print("You have successfully created an account.")
                break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        print("\nMENU:")
        print("1. View Diseases and Doctors")
        #print("2. Assign Doctor to Patient")
        print("2. Prompt User for Disease and Doctor Assignment")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            view_diseases_and_doctors()
        elif choice == '2':
            prompt_user_for_disease()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")