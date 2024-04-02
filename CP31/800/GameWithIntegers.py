def main():
    t = int(input())
    while t > 0:
        n = int(input())
        if n % 3 == 0:
            print("Second")
        else:
            print("First") 
        t -= 1


if __name__ == '__main__':
    main()