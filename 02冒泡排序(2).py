class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def main():
    a = []
    total = int(input('The total num:'))

    # 在a列表中储存指定数目的对象
    for index in range(total):
        name = input('The name of No.%d student:' % (index + 1))
        score = input('The score of No.%d student:' % (index + 1))
        stu = Student(name, score)
        a.append(stu)

    # 冒泡排序核心代码
    for i in range(total - 1):
        for j in range(total - i - 1):
            if a[j].score < a[j + 1].score:
                temp = a[j].score
                a[j].score = a[j + 1].score
                a[j + 1].score = temp

    # 输出排名
    for i in range(total):
        print('name: ', a[i].name, ' score: ', a[i].score)


if __name__ == '__main__':
    main()
