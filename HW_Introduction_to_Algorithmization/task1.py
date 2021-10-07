import functools

def main():
    list_num = list(map(int, str(input())))
    if len(list_num) != 3:
        print("Must be three-digit!")
        return 1
    else:
        print(f'sum = {sum(list_num)}')
        print(f'mul = {functools.reduce(lambda a, b : a * b, list_num)}')

if __name__ == '__main__':
    main()