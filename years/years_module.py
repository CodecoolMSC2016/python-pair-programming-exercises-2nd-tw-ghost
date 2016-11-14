import datetime


def years(age):
    year_of_100 = (100 - age) + int(datetime.date.today().strftime("%Y"))
    for i in range(int(input("Enter number: "))):
        print('You will be 100 in the year:', year_of_100)
    return year_of_100


def main():
    return

if __name__ == '__main__':
    main()
