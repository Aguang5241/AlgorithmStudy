class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def main():
    a = []
    total = int(input('The total num:'))

    for index in range(total):
        name = input('The name of No.%d student:' % (index + 1))
        score = input('The score of No.%d student:' % (index + 1))
        stu = Student(name, score)
        a.append(stu)

    for item in a:
        print(item.__dict__)


if __name__ == '__main__':
    main()
