def listoverlap(list1, list2):
    import itertools

    c = []
    for i in itertools.chain(list1, list2):
        if i in list1 and i in list2:
            c.append(i)

    return list(set(c))


def main():
    return

if __name__ == '__main__':
    main()
