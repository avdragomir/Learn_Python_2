msg = "What's up?"
print(msg)
def least_diff(a,b,c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)
x = least_diff(5,4,1)
print(x)

)