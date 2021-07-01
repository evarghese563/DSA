#!/bin/python3
def getWays(n, c):
    # Write your code here

    coin = len(c)

    Matrix = [[0 for x in range(n+1)] for y in range(coin)]

    for i in range(0,coin):

        Matrix[i][0] = 1

        if i == 0:
            for j in range(1,n+1):
                if (j%c[i] == 0):
                    Matrix[0][j] = 1
                else:
                    Matrix[0][j] = 0
        else:
            for k in range(1,n+1):
                if c[i]>k:
                    Matrix[i][k] = Matrix[i-1][k]
                else:
                    Matrix[i][k] = Matrix[i-1][k]+Matrix[i][k-c[i]]


    return Matrix[coin-1][n]




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

c = list(map(int, input().rstrip().split()))

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

ways = getWays(n, c)
print(ways)
