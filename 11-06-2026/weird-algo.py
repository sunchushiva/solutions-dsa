stdin = int(input())


def weird_algorithm(n):

    output = f"{n}"

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        output += " " + f"{n}"
    print(output)
    return None


weird_algorithm(stdin)
