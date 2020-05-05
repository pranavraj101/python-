sum=0
def sum1(n):
    global sum
    if n==1:
        return 1
    sum=n+sum1(n-1)
    return(sum)
