
def min_path(triangle):

    s = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            s[j] = triangle[i][j] + min(s[j], s[j + 1])
    return s[0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print("Минимальная сумма пути:", min_path(triangle))
