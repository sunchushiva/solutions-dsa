output = []
input_lines = 2
line = 0

while line != input_lines:
    stdin = input()
    output.append(stdin)
    line += 1

n = int(output[0])
array = [int(i) for i in output[1].split(" ")]


def increasing_array(n, arr):

    steps = 0

    for a in range(1, n):

        if arr[a] >= arr[a - 1]:
            continue
        else:
            steps += arr[a - 1] - arr[a]
            arr[a] = arr[a - 1]

    print(steps)

    return None


increasing_array(n, array)
