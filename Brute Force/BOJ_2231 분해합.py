def main():
    st = int(input())
    for i in range(st):
        k = str(i)
        sum = int(i)
        for s in range(len(k)):
            sum += int(k[s])
        if sum == st:
            print(int(i))
            return 0

    print(0)


main()
