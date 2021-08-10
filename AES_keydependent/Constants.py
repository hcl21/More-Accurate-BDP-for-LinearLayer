P = [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3]
state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
NUMBER = 17

S_T = [
    [1, 1, 1, 1, 40, 1, 1, 1, -7, -6, -7, -7, -6, -7, -7, -6, 6],
    [1, 1, 1, 1, 1, 35, 1, 1, -5, -6, -6, -6, -6, -6, -6, -6, 5],
    [0, 0, 0, 0, 0, 0, 10, 0, -1, -1, -2, -2, -2, -2, -1, -1, 2],
    [1, 1, 1, 33, 1, 1, 1, 1, -6, -7, -7, -6, 0, -7, -7, -6, 6],
    [0, 0, 0, 0, -1, 0, 0, 17, -1, -3, -4, -1, -4, -2, -4, -2, 5],
    [61, 2, 13, 2, 2, 2, 2, 2, -12, -11, -12, -13, -12, -13, -13, -11, 11],
    [0, 13, 0, 0, 0, 0, 0, 0, -2, -1, -2, -2, -4, -4, -1, -1, 4],
    [-29, -29, -26, -30, -36, -37, -29, -35, 9, 1, 11, 7, 5, 2, 2, -6, 220],
    [-2, -1, -4, -5, -7, -6, -3, -6, 27, 29, 31, 31, 33, 33, 32, 28, 0],
    [-1, 0, 17, 0, 0, 0, 0, 0, -2, -3, -3, -5, -5, -1, -1, -2, 6],
    [1, -8, 0, 0, 1, 1, -4, -3, -4, -7, -3, -12, -8, 4, -13, 27, 28],
    [3, 1, 0, 0, 0, 15, 0, 0, -8, -10, -12, -11, 42, -14, -9, -11, 14],
    [1, 0, 3, 3, 0, 0, 11, 2, -9, -11, 36, -10, -10, -8, -9, -10, 11],
    [0, -1, -2, -6, -4, -6, -3, -6, 3, 2, 4, 4, 3, 1, 1, -5, 27],
    [-1, -1, -3, -2, -1, -8, -2, 5, -6, -7, 2, 7, -4, -6, 2, 2, 23],
    [-1, -2, -2, 0, -4, -1, -2, -2, 3, 1, -2, 5, -4, -3, -2, 5, 16],
    [1, -1, -6, 0, 0, 0, -9, 3, -14, 8, -11, -4, 8, 3, -13, 5, 30],
    [1, 3, 1, -2, 0, 0, 0, -2, 3, 5, -4, -10, 3, -10, 5, -7, 14],
    [-2, -2, 1, -2, -2, 0, -2, 1, -4, 1, -1, 3, 0, 3, 3, -2, 12],
    [1, 0, 1, 4, 0, 0, -1, 0, 1, -7, 0, 9, -5, 2, -7, -6, 8],
    [-2, -6, -9, -12, -10, -9, -10, -8, 3, 1, 7, 4, 10, 11, 11, 4, 53],
    [-7, -4, -8, -3, -8, -8, -8, -1, 6, 7, 9, 2, 9, 6, 9, 5, 37],
    [1, -2, -2, -2, 1, -2, -2, -2, -2, 1, 3, 0, -4, -2, -2, 3, 14],
    [-2, -2, 0, -1, 0, -1, -1, -2, -1, 1, -2, -1, 1, -1, 1, 1, 10],
    [1, 1, -6, -1, 0, 0, -3, 0, -4, 3, 2, 2, 2, -3, -4, -3, 14],
    [-3, -1, -1, -3, -3, -3, -1, -3, 16, 16, 17, 17, 17, 17, 15, 15, 0],
    [1, 3, 5, 0, 5, 4, 3, 2, -19, -18, 41, -20, -20, -2, -3, -2, 20],
    [-5, -3, -4, -2, -5, -3, -1, -1, 2, -2, -1, 2, -1, 2, 1, -3, 24],
    [-2, -3, -1, -1, -2, 1, -1, -1, -5, 2, -3, 0, 2, 0, 0, 0, 14],
    [-3, -1, -4, -4, -1, -3, -4, 0, 1, -2, 3, 4, 3, 1, 2, 3, 18],
    [-2, -2, 4, -1, -2, -2, -2, -1, -1, -1, -3, -2, -1, -4, 3, 3, 14],
    [-1, -1, 2, -2, -2, -2, -2, -2, 1, 1, -4, -1, -2, -3, 2, 2, 14],
    [-2, -4, -2, -1, -1, -2, -1, 2, 1, 1, -1, 1, -1, 2, -3, -5, 16],
    [2, 0, -2, -1, -1, -1, -1, -1, 2, -3, -1, 1, 1, -1, -2, -1, 9],
    [-1, -1, -1, -2, 0, 0, -1, -1, 1, 1, 1, 1, -3, -2, -2, 1, 9],
]

