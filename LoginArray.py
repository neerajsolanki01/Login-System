# I can Use list here to store user info name and pass
# List to store user credentials as lists [username, password, info]
users = [['neeraj', 'neer1234', {'Name': 'Neeraj Solanki', 'Age': 21, 'Gender': 'Male'}],
         ['madhav', 'madhav1234', {'Name': 'Madhav Jha', 'Age': 20, 'Gender': 'male'}]]


def display_user_info(user_info):
    print("Name:", user_info['Name'])
    print("Age:", user_info['Age'])
    print("Gender:", user_info['Gender'])


def update_user_info(user_info):
    new_name = input("Enter your full name (leave blank to keep current): ")
    new_age = input("Enter your age (leave blank to keep current): ")
    new_gender = input("Enter your gender (leave blank to keep current): ")

    if new_name:
        user_info['Name'] = new_name
    if new_age:
        user_info['Age'] = int(new_age)
    if new_gender:
        user_info['Gender'] = new_gender

    print("User information updated successfully!")


def delete_user_info(username):
    for user in users:
        if user[0] == username:
            users.remove(user)
            print("User information deleted successfully!")
            break
    else:
        print("User not found.")


def func():
    while True:
        user_type = input("Are you a new user or an existing user? (Type 'new' or 'existing' or 'break'): ")

        if user_type.lower() == 'new':
            new_name = input("Enter your username: ")
            new_password = input("Enter your password: ")
            full_name = input("Enter your full name: ")
            new_age = int(input("Enter your age: "))
            new_gender = input("Enter your gender: ")

            # Storing the new user as a list in the list
            users.append([new_name, new_password, {'Name': full_name, 'Age': new_age, 'Gender': new_gender}])
            print("New user created successfully!")

        elif user_type.lower() == 'existing':
            input_name = input("Enter your username: ")
            input_password = input("Enter your password: ")

            # Checking if the entered username and password exist in the list
            for user in users:
                if user[0] == input_name and user[1] == input_password:
                    print("Login successful!")
                    display_user_info(user[2])

                    action_choice = input("Do you want to update, delete, or do nothing? (Type 'update', 'delete', or 'nothing'): ")

                    if action_choice.lower() == 'update':
                        update_user_info(user[2])
                    elif action_choice.lower() == 'delete':
                        delete_user_info(input_name)
                    break
            else:
                print("Invalid username or password. Please try again.")

        elif user_type.lower() == 'break':
            break

        else:
            print("Invalid choice. Please choose 'new' or 'existing'.")

func()