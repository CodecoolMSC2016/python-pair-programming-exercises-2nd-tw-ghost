def passwordgen(pw_strength=''):
    import string
    import random

    password = []

    lower_case_letters = list(string.ascii_lowercase)
    upper_case_letters = list(string.ascii_uppercase)
    symbols = list('!@#$%^&*()?')
    numbers = list(string.digits)
    words = list(('''Lorem ipsum dolor sit amet, consectetur adipiscing elit Fusce vulputate 
                    ex in posuere pulvinar Duis sed dapibus urna Curabitur sit''').split())

    if pw_strength.lower() == 'strong' or pw_strength.lower() == '':
        for i in [0, 1]:
            password.append(random.choice(lower_case_letters) + random.choice(upper_case_letters)
                            + random.choice(symbols) + random.choice(numbers))
    elif pw_strength.lower() == 'weak':
        for i in [0, 1]:
            password.append(random.choice(words))

    return '' .join(password)


def main():
    return


if __name__ == '__main__':
    main()
