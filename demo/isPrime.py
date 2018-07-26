# 求素数 素数为在大于1的自然数中，除了1和它本身以外不再有其他因数


def is_prime(num):
    for i in range(2, num):
        # 如果从2开始到num区间内,存在一个取余为0的数字
        # 说明这个数被num整除,则num不为素数
        if(num % i) == 0:
            return False
    return True


def get_primes(max_num):
    primes = []
    for num1 in range(2, max_num):
        if is_prime(num1):
            primes.append(num1)
    return primes


# 输出所有小于maxNum的素数
maxNum = int(input("请输入您要判定的数字:"))

listOfPrimes = get_primes(maxNum)
print(listOfPrimes)

