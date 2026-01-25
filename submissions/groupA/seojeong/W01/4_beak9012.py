n = int(input().strip())

for _ in range(n):
    s = input().strip()

    while "()" in s:
        s = s.replace("()", "")

    if len(s) == 0:
        print("YES")
    else:
        print("NO")