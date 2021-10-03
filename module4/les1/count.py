import os


def read_line(path):
    lst = []

    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            lst.append(int(line.strip()))

    return lst


def count_sum(ints):
    print('Started count')
    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 10000:
                    counter += 1
                    print('Found')

    print(f'counting end: {counter}')
    return counter


if __name__ == '__main__':
    ints = read_line(os.path.abspath('data.txt'))

    count_sum(ints)

    print(input('Are you ok with it? [y/n]?'))

    print('end name')