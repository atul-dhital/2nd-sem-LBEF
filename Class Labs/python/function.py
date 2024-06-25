#with parameter with return type
def rev(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev
n = int(input("Enter the number: "))
print(rev(n))

#without parameter with return type
def rev():
    n = int(input("Enter the number: "))
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev
print(rev())
