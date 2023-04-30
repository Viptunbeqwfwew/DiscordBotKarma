env = {}

def first_run():
    with open(".env", "w+") as f:
        env["TOKEN"] = input("Введите токен бота: ")
        f.write("\n".join([i + "=" + env[i] for i in env]))


try:
    with open(".env", "r") as f:
        env = {i[0:i.find("=")]: i[i.find("=") + 1:] for i in f.read().split("\n")}
except:
    first_run()

TOKEN = env["TOKEN"]