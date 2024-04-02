def main():
    t = int(input())
    while t > 0:
        n = int(input())
        s = input()
        count = 0
        for i in range(0, n):
            if i < n - 2 and s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
                count = 2
                break
            elif s[i] == '#':
                continue
            elif s[i] == '.':
                count += 1
        print(count)
        t -= 1
if __name__ == '__main__':
    main()