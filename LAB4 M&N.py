# Python3 to find Product of
# 2 Numbers using Recursion

# recursive function to calculate
# multiplication of two numbers
def product(m, n):
    # if x is less than y swap
    # the numbers
    if m < n:
        return product(m, n)

    # iteratively calculate y
    # times sum of x
    elif n != 0:
        return (m + product(m, n - 1))

    # if any of the two numbers is
    # zero return zero
    else:
        return 0


# Driver code
m = 5
n = 2
print(product(m, n))