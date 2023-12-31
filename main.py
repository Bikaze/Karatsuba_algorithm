def mul(num1, num2):
    """ Multiplies two numbers using Karatsuba algorithm """
    len1 = len(str(num1))
    len2 = len(str(num2))

    if len1 == 1 and len2 == 1:
        return num1 * num2

    len_a = len1 if len1 > len2 else len2
    half = len_a // 2

    a = num1 // pow(10, half)
    b = int(num1 % pow(10, half))
    c = num2 // pow(10, half)
    d = int(num2 % pow(10, half))

    ac = mul(a, c)
    bd = mul(b, d)
    ad_bc = mul(a + b, c + d) - ac - bd

    if len_a % 2 == 1:
        answer = pow(10, (len_a - 1)) * ac + pow(10, half) * ad_bc + bd
    else:
        answer = pow(10, len_a) * ac + pow(10, half) * ad_bc + bd

    return answer


print(mul(3141592653589793238462643383279502884197169399375105820974944592,
          2718281828459045235360287471352662497757247093699959574966967627))
