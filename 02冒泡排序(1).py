import numpy as np


def main():
    testArray = np.random.randint(0, 10, 10)
    length = len(testArray)
    print(testArray)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if testArray[j] < testArray[j + 1]:
                temp = testArray[j]
                testArray[j] = testArray[j + 1]
                testArray[j + 1] = temp

    print(testArray)


if __name__ == '__main__':
    main()

# [4 2 5 3 7 4 1 1 2 4]
# [7 5 4 4 4 3 2 2 1 1]
