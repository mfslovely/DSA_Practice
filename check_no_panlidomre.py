def is_palidorme(n):
    num = n

    result = 0

    while num>0:
        last_digit = num%10
        result = (result*10)+last_digit
        num = num//10
    if result == n:
        return True
    else:
        return False
n = 1587
print(is_palidorme(n))