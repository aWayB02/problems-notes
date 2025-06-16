def solve(a):

    while a >= 0:

        if a % 111 == 0:

            return "YES"

        a -= 11

    return "NO"
