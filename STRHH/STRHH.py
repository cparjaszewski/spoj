import sys

t = int(input())
while t > 0:
    t -= 1
    line = sys.stdin.readline()
    halfline = line[:len(line)/2]
    secondhalfline = halfline[::2]
    print(secondhalfline)
