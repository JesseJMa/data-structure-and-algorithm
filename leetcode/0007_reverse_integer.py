def reverse(x: int) -> int:
    sign = x < 0 and -1 or 1
    ans = 0
    x = abs(x)
    while x:
        ans = ans * 10 + x % 10
        x //= 10
    return sign * ans if x < 0x7fffffff else 0
    pass

print(reverse(-123))