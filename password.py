MASTER_PASSWORD = "pallavi"

pwd = input("Enter Master Password: ")

if pwd != MASTER_PASSWORD:
    print("Wrong Password")
    exit()


def view():

    try:
        with open("password.txt", "r") as f:

            data = f.readlines()

            if len(data) == 0:
                print("No passwords saved")

            for line in data:

                user, password = line.rstrip().split("|")

                print("\nAccount :", user)
                print("Password :", password)
                print("-------------------")

    except FileNotFoundError:
        print("No password file found")


def add():

    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:

        f.write(name + "|" + pwd + "\n")

    print("Password Added Successfully")


def search():

    account = input("Search Account Name: ")

    try:

        with open("password.txt", "r") as f:

            found = False

            for line in f:

                user, password = line.rstrip().split("|")

                if user.lower() == account.lower():

                    print("\nPassword:", password)

                    found = True

            if found == False:
                print("Account Not Found")

    except:
        print("Error")


while True:

    print("""

======= PASSWORD MANAGER =======

1. Add Password
2. View Password
3. Search Password
q. Exit

===============================
""")

    mode = input("Enter Option: ")

    if mode == "1":
        add()

    elif mode == "2":
        view()

    elif mode == "3":
        search()

    elif mode == "q":
        print("Program Closed")
        break

    else:
        print("Invalid Option")