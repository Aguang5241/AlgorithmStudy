import numpy as np


def main():
    a = []
    testArray = np.random.randint(0, 10, 10)
    result = []

    # 初始化所有“桶”的值为0
    for i in range(len(testArray)):
        a.append(0)

    # 循环读入测试集数据，并进行计数
    for item in testArray:
        a[item] += 1

    # 依次判断所有的“桶”，出现几次就输出到列表几次
    for i in range(len(a)):
        for times in range(a[i]):
            result.append(i)

    print(testArray)
    print(a)
    print(result)


if __name__ == '__main__':
    main()
# [5 6 7 9 2 7 7 1 5 1]
# [0, 2, 1, 0, 0, 2, 1, 3, 0, 1]
# [1, 1, 2, 5, 5, 6, 7, 7, 7, 9]