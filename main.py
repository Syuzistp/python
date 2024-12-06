def josephus(n, k):
    n = list(range(1,n+1))
    ans = []
    i = 0
    while n:
        i = (i + k - 1) % len(n)
        ans.append(n.pop(i))
    return ans





if _