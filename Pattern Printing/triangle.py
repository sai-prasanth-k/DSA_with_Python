def triangle_pattern(N):
    for i in range(1, N):
        for space in range(N - i):
            print(" ", end='')
        for star in range(2 * i - 1):
            print("*", end="")

        print()

    return


def main():
    n = int(input())
    triangle_pattern(n)


main()
