import numpy as np


def main():
    def quick_sort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i < pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quick_sort(less) + [pivot] + quick_sort(greater)

    raw_arr = np.linspace(0, 100, 50, dtype=int)
    arr = np.random.choice(raw_arr, 10)
    print(arr)
    print(quick_sort(arr))


if __name__ == '__main__':
    main()
