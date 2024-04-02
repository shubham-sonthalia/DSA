def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()[:n]))
        if arr[0] != 1:
            print("NO")
        else:
            notPossible = False
            for i in range(1, n - 1):
                if arr[i] != i  + 1 and arr[i + 1] != i + 1:
                    notPossible = True
                    break
                elif arr[i + 1] == i + 1 and arr[i] == i + 2:
                    i = i + 1
            if notPossible:
                print("NO")
            else:
                print("YES")
        t -= 1

if __name__ == '__main__':
    main()