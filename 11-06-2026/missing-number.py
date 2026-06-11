output = []
input_lines = 2
line = 0

while line != input_lines:
    stdin = input()
    output.append(stdin)
    line += 1

n = int(output[0])
array = [int(i) for i in output[1].split(" ")]


def missing_number(n):

    real = (n * (n + 1)) // 2
    calc = 0

    for a in range(0, len(array)):
        calc += array[a]

    print(real - calc)
    return None


missing_number(n)
