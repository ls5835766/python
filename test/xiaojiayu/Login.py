# 模拟登陆的实现

user_date = {}


def new_user():
    prompt = "请输入用户名"
    while True:
        name = input(prompt)
        if name in user_date:
            prompt = "此用户已经被使用，请重新输入:"
            continue
        else:
            break

    password = input("请输入密码:")
    user_date[name] = password
    print("注册成功，赶紧试试登录吧！")


def old_user():
    prompt = "请输入用户名"
    while True:
        name = input(prompt)
        if name not in user_date:
            prompt = "您输入的用户名不存在，请重新输入:"
            continue
        else:
            break
    password = input("请输入密码:")
    pwd = user_date.get(name)

    if password == pwd:
        print("登录成功！")
    else:
        print("密码错误")


def showmenu():
    propmt = '''
    | - - - 新建用户：n/N - - - |
    | - - - 登录账户：e/E - - - |
    | - - - 退出程序：q/Q - - - |
    | - - -  请输入指令代码:
    '''

    while True:
        chose = False

        while not chose:
            choice = input(propmt)
            if choice not in "NnEeQq":
                print("您输入的指令有误")
            else:
                chose = True

            if choice == "q" or choice == "Q":
                break
            if choice == "n" or choice == "N":
                new_user()
            if choice == "e" or choice == "E":
                old_user()


showmenu()
