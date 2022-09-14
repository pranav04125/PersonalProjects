from operator import le


def perimeter(length, breadth):
    return (length + breadth)*2

def main():
    a = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    print("Perimeter is", perimeter(a, b))

main()