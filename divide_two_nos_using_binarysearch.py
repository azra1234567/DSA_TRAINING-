def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError

    low, high = 0, dividend
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * divisor <= dividend:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
