from random import randint, uniform
from string import ascii_lowercase

class RandomVal:
    def __init__(self):
        self.borders = list()

    def input_borders(self):
        self.borders = str(input("Enter left & right border, format X,Y\n")).split(',')

    def board_check(self)
        if (len(list_num) != 2) and (list_num[0] > list_num[1]):
            print("Invalid border values!")
            return False
        else:
            return True

def main():
    list_num = list(map(int, str(input()).split(',')))
    if board_check():
        return 1
    else:
        print(f'{random integer: list_num[0]} < {randint(list_num[0], list_num[1])} < {list_num[1]}')
        print(f'{random float: list_num[0]} < {uniform(float(list_num[0]), float(list_num[1]))} < {list_num[1]}')
        print(f'')

if __name__ == '__main__':
    main()