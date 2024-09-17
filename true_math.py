
def true_divide(first, second):
    import math
    if second == 0:
        return math.inf
    return first/second

result1 = true_divide(49, 7)
print(result1)
result2 = true_divide(15, 0)
print(result2)
