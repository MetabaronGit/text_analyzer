from task_template import TEXTS

LINE_SEPARATOR = "-" * 50
login_tab = dict(bob="123",
                 ann="pass123",
                 mike="password123",
                 liz="pass123")

login_name = str(input("Zadej svoje přihlašovací jméno: "))
login_password = str(input("Heslo: "))
print(LINE_SEPARATOR)

if login_tab.get(login_name) == login_password:
    print("Vítej v aplikaci, {0}.".format(login_name))
    print("Počet připravených textů k analýze: {0}".format(len(TEXTS)))
    print(LINE_SEPARATOR)
    text_id = int(input("Který text chceš analyzovat? Zadej číslo 1 - 3: "))
    print(LINE_SEPARATOR)

    if text_id in range(1, 4):
        #hlavní analýza
        word_list = TEXTS[text_id - 1].split()
        for i in range(len(word_list)):
            word_list[i] = word_list[i].strip(" \".,")

        len_occurences = dict()
        analyzed_words = dict()

        for word in word_list:
            analyzed_words["total_words"] = analyzed_words.get("total_words", 0) + 1
            if word.istitle():
                analyzed_words["titlecase_words"] = analyzed_words.get("titlecase_words", 0) + 1
            if word.isupper():
                analyzed_words["uppercase_words"] = analyzed_words.get("uppercase_words", 0) + 1
            if word.lower():
                analyzed_words["lowercase_words"] = analyzed_words.get("lowercase_words", 0) + 1
            if word.isnumeric():
                analyzed_words["numbers"] = analyzed_words.get("numbers", 0) + 1
                analyzed_words["numbers_sum"] = analyzed_words.get("numbers_sum", 0) + int(word)
            len_occurences[f"{len(word)}"] = len_occurences.get(f"{len(word)}", 0) + 1

        print("Ve vybraném textu je celkem {0} slov.".format(analyzed_words.get("total_words")))
        print("Slov začínajících velkým písmenem je {0}.".format(analyzed_words.get("titlecase_words")))
        print("Slov napsaných pouze velkými písmeny je {0}.".format(analyzed_words.get("uppercase_words")))
        print("Slov napsaných pouze malými písmeny je {0}.".format(analyzed_words.get("lowercase_words")))
        print("Počet čísel v textu je {0}.".format(analyzed_words.get("numbers")))
        print("Součet všech čísel v textu je {0}.".format(analyzed_words.get("numbers_sum")))
        print(LINE_SEPARATOR)

        #vykreslení grafu
        OCCURENCES_COLUMN_WIDTH = 20

        print("DÉLKA | VÝSKYT" + " " * (OCCURENCES_COLUMN_WIDTH - 7) + " | POČET")
        print(LINE_SEPARATOR)

        key = 1
        while len_occurences:
            if len_occurences.get(f"{key}") is not None:
                len_string = " " * (5 - len(str(key))) + str(key)
                graph_gauge = "*" * (len_occurences.get(f"{key}") % OCCURENCES_COLUMN_WIDTH)
                print(len_string + " |" + graph_gauge + " " * (OCCURENCES_COLUMN_WIDTH - len(graph_gauge)) +
                      " | " + str(len_occurences.get(f"{key}")))
                len_occurences.pop(f"{key}")
                key += 1

    else:
        print("Špatně zvolené číslo textu.")

else:
    print("Nesprávné jméno nebo heslo. Přístup zamítnut!")
