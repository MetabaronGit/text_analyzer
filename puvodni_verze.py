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
    text_id = input("Který text chceš analyzovat? Zadej číslo 1 - 3: ")
    print(LINE_SEPARATOR)

    if text_id.strip() in ("1", "2", "3"):

        #hlavní analýza
        analyzed_words = dict(total_words=0,
                              titlecase_words=0,
                              uppercase_words=0,
                              lowercase_words=0,
                              numbers=0,
                              numbers_sum=0)
        actual_word = ""
        len_occurences = dict()

        for char in TEXTS[int(text_id) - 1]:
            if char.isalnum():
                actual_word += char
            else:
                if actual_word != "":
                    analyzed_words["total_words"] += 1
                    if actual_word.isalpha():
                        if actual_word[0].isupper():
                            analyzed_words["titlecase_words"] += 1
                        if actual_word.isupper():
                            analyzed_words["uppercase_words"] += 1
                        if actual_word.islower():
                            analyzed_words["lowercase_words"] += 1
                    if actual_word.isnumeric():
                        analyzed_words["numbers"] += 1
                        analyzed_words["numbers_sum"] += int(actual_word)

                    if len_occurences.get(str(len(actual_word))) is not None:
                        len_occurences[str(len(actual_word))] += 1
                    else:
                        len_occurences[str(len(actual_word))] = 1
                    actual_word = ""

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

        # tady by se mi líbil víc cyklus "while", ale zatím neumím ;)
        MAX_WORD_LENGHT = 50
        for key in range(1, MAX_WORD_LENGHT):
            if len_occurences.get(str(key)) is not None:
                len_string = " " * (5 - len(str(key))) + str(key)
                graph_gauge = "*" * (len_occurences.get(str(key)) % OCCURENCES_COLUMN_WIDTH)
                print(len_string + " |" + graph_gauge + " " * (OCCURENCES_COLUMN_WIDTH - len(graph_gauge)) + " | " + str(len_occurences.get(str(key))))

    else:
        print("Špatně zvolené číslo textu.")

else:
    print("Nesprávné jméno nebo heslo. Přístup zamítnut!")