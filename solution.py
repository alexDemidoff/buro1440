def min_path(triangle):

    s = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            s[j] = triangle[i][j] + min(s[j], s[j + 1])
    return s[0]
