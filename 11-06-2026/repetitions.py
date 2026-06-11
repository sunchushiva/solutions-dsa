stdin = input()
n = len(stdin)


def repetitions(n, str):
    max = 1
    count = 1

    for a in range(1, n):

        if str[a] == str[a - 1]:
            count += 1
        else:
            if count > max:
                max = count

            count = 1

    if count > max:
        max = count

    print(max)
    return None


repetitions(n, stdin)
