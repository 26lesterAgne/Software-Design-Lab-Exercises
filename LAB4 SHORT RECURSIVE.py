def mult(m, n):
        def mul(m, n):
        return m if n == 1 else m + (m, n - 1)
    else:
        return result


m = int(input())
n = int(input())
print(mult(m, n))