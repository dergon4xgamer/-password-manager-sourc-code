command = input("etern the command")
if "password show" in command:
    d = open("password.txt","r")
    read = d.readlines(9999999998)
    print(read)
if "set password" in command:
    password_name = input("etern the password name")
    password = input("enter the password")
    f = open("password.txt","w")
    f.write("password is "+  password)
    f.write("password name"+ password_name)