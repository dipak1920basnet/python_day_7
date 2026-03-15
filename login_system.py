# Unguided Challenges
def main():
    users = {
        "dipak": "pass123",
        "admin": "admin123",
        "guest": "guest123"
    }

    user_name = get_username()
    password = get_password()

    if validation(users, user_name, password):
        print("Login successful")
    else:
        print("Invalid credentials")

def validations(name, type):
    if isinstance(name, type):
        return True
    else:
        return False
    
def get_username():
    while True:
        username = input("Enter your username: ")
        if validations(username, str):
            return username
        else:
            print("Username must be of string")

def get_password():
    while True:
        password = input("Enter your password: ")
        if validations(password, str):
            return password
        else:
            print("password must be of string")
def validation(data_set, username, password):
    try:
        passes = data_set[username]
    except KeyError:
        print("incorrect username")
    else:
        if passes == password:
            return True
    return False

if __name__ == "__main__":
    main()