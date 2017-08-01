import sys

t = int(input())
while t > 0:
    t = t - 1
    line = sys.stdin.readline().strip()
    half_line = line[:len(line)/2]
    even_half_line = half_line[0:len(half_line):2]
    print(even_half_line)
