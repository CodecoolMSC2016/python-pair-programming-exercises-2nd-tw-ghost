def palindrome(str):
    str = ("" .join(str.split())).lower()
    for i in range(0, len(str)):
        if str[i] != str[(i + 1) * -1]:
            print(str[i], str[i])
            return False
    return True


def main():
    palindrome("A nut for a jar of tuna")
    return


if __name__ == '__main__':
    main()
