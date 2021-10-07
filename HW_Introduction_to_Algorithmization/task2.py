def main():
    print(f"OR 5|6 = {5|6}\n returns 1 if any of the bits are 1. If both bits are 0, it returns 0")
    print(f"AND 5&6 = {5&6}\n returns 1 if both bits are 1, otherwise 0")
    print(f"XOR 5^6 = {5^6}\n returns 1 if one of the bits is 0 and the other bit is 1. If both bits are 0 or 1, it returns 0.")
    print(f"OnesCompliment ~5 = {~5}\n the complement of a number is equal to the negative sum of the number plus one")
    print(f"LeftShift 5<<2 = {5<<2}\n add zeros to the left of the bit representation")
    print(f"RightShift 5>>2 = {5>>2}\n add zeros to the right of the bit representation")

    
if __name__ == '__main__':
    main()