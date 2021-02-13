from task_template import TEXTS
LINE_SEPARATOR = "-" * 50

login_tab = dict(bob = "123", ann = "pass123", mike = "password123", liz = "pass123")
login_name = str(input("Zadej svoje přihlašovací jméno: "))
login_password = str(input("Heslo: "))
print(LINE_SEPARATOR)

if login_tab.get(login_name) == login_password:
    print("Vítej v aplikaci, {0}.".format(login_name))
    print("Počet připravených textů k analýze: {0}".format(len(TEXTS)))
    print(LINE_SEPARATOR)
    text_id = input("Který text chceš analyzovat? Zadej číslo 1 - 3: ")
    print(LINE_SEPARATOR)

    if text_id.strip() in ("1", "2", "3"):

        #hlavní analýza
        total_words = 0
        titlecase_words = 0
        uppercase_words = 0
        lowercase_words = 0
        numbers = 0
        numbers_sum = 0
        actual_word = ""

        for char in TEXTS[int(text_id) - 1]:
            if char.isalnum():
                actual_word += char
            else:
                if actual_word != "":
                    total_words += 1
                    if actual_word.isalpha():
                        if actual_word.istitle():
                            titlecase_words += 1
                        if actual_word.isupper():
                            uppercase_words += 1
                        if actual_word.islower():
                            lowercase_words += 1
                    if actual_word.isnumeric():
                        numbers += 1
                        numbers_sum += int(actual_word)
                    actual_word = ""

        print("Ve vybraném textu je celkem {0} slov.".format(total_words))
        print("Slov začínajících velkým písmenem je {0}.".format(titlecase_words))
        print("Slov napsaných pouze velkými písmeny je {0}.".format(uppercase_words))
        print("Slov napsaných pouze malými písmeny je {0}.".format(lowercase_words))
        print("Počet čísel v textu je {0}.".format(numbers))
        print("Součet všech čísel v textu je {0}.".format(numbers_sum))
        print(LINE_SEPARATOR)

        #vykreslení grafu
        print("DÉLKA | VÝSKYT        | POČET")
        print(LINE_SEPARATOR)
        for i in range(6,15):
            len_string = " " * (5 - len(str(i))) + str(i)
            print(len_string + " |" + " " * 14 + " |")

    else:
        print("Špatně zvolené id číslo textu.")

else:
    print("Nesprávné jméno nebo heslo. Přístup zamítnut!")


print("konec")