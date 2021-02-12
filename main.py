from task_template import TEXTS

login_tab = dict(bob = "123", ann = "pass123", mike = "password123", liz = "pass123")
login_name = str(input("Zadej svoje přihlašovací jméno: "))
login_password = str(input("Heslo: "))

if login_tab.get(login_name) == login_password:
    print("Dobrý den {0}, analyzátor textu je připraven.\n".format(login_name))


else:
    print("Nesprávné jméno nebo heslo. Přístup zamítnut!")

 # print(login_tab[login_name])