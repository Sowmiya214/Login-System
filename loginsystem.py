def mail(username):
    import re
    regex = r'[a-z]+[a-z.|0-9]+@[a-za-z]+[.]+.[a-z]{,}'
    if (re.fullmatch(regex, username)):
        return True
    else:
        return False

def pswd(password):
    import re
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#%*?&])[A-Za-z\d#@$!%*?&]{5,16}$"
    if (re.fullmatch(regex, password)):
        return True
    else:
        return False


db = open('database.txt','r')
u = []
p = []
for x in db:
    a, b = x.split(',')
    b = b.strip()
    u.append(a)
    p.append(b)


def Login():
    username = input('Enter your username: ')
    if username in u:
        A = u.index(username)
        B = p[A]
        password = input('Enter your password: ')
        if password == B:
            print('Login Successfully!')
            z = "Hi {}, Welcome to GUVI...!"
            print(z.format(username))
        else:
            print("password doesn't exist")
            reset()
    else:
        print("username doesn't exist!")
        home()


def Register():
    username = input('Create a new username: ')
    if mail(username)==False:
        print("Invalid username")
        Register()
    password = input('Create a new password: ')
    if pswd(password)==False:
        print("Invalid password")
        Register()
    if username not in u:
        u.append(username)
        p.append(password)
        db = open('database.txt', 'a')
        print('Registered Successfully!')
        update()
        home()
    else:
        print("username exist!")
        Register()

def forgotpswd():
    username = input('Enter your username: ')
    if username in u:
        Q=u.index(username)
        password = input("Create your new password: ")
        if pswd(password) == True:
            p[Q] = password
            print("password successfully changed!")
            update()
        else:
            print("Invalid password!")
            forgotpswd()
    else:
        print('Invalid username!')
        forgotpswd()



def update():
    db = open('database.txt', 'w')
    for x in range(len(u)):
        db.write(u[x] + "," + p[x] + "\n")


def reset(option=None):
    option = input('Login | Forgotpassword: ')
    if option == 'Login':
        Login()
    elif option == 'Forgotpassword':
        forgotpswd()
    else:
        print('Please enter the option')
        reset()


def home(option=None):
    option = input('Login | Register: ')
    if option == 'Login':
        Login()
    elif option == 'Register':
        Register()
    else:
        print('Please enter the option')
        home()
home()












