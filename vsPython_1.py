msg = "What's up?"
print(msg)
def least_diff(a,b,c):
    """ Definition. 
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)
x = least_diff(5,4,1)
print(x)

print(
    least_diff(100, 2, 98),
    least_diff(54, 564, 645),
    least_diff(875, 423, 876)
)


def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)