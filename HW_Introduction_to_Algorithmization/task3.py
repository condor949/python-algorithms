def main():
    pointA = str(input("Enter the first point, format X,Y\n")).split(",")
    pointB = str(input("Enter the second point, format X,Y\n")).split(",")
    pointA = list(map(int, pointA))
    pointB = list(map(int, pointB))

    if (len(pointA) != 2) and (len(pointB) != 2):
        print("Wrong input data format!")
        return 1
    k = (pointB[1] - pointA[1])/(pointB[0] - pointA[0])
    b = (pointB[0]*pointA[1] - pointB[1]*pointA[0])/(pointB[0] - pointA[0])
    print(f"Line function: y = {k}x + {b}")

if __name__ == '__main__':
    main()