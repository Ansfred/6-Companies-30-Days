class Solution:
    def trailingZeroes(self, n: int) -> int:
        ''' Time Complexity - O(n)
        if n == 0 or n == 1:
            return 0

        factorial = 1
        while n != 1:
            factorial *= n
            n -= 1

        factorial = str(factorial)
        x = len(factorial) - 1
        number_of_trailingZeroes = 0
        while x >= 0:
            if factorial[x] == '0':
                number_of_trailingZeroes += 1
                x -= 1
            else:
                break
        
        return number_of_trailingZeroes
        '''

        # Follow Up: Time Complexity - O(log n)
        # 0's -> 2's * 5's. Since, plenty of 2's are present(EVEN NUMBERS); 5's are the deciding factor. In 5!: number of 0's = 1, in 10!: number of 0's = 2. Therefore, number of 0's in n! => number of 5's in n. For example: 5!(`5` * 4 * 3 * 2 * 1), 10!(`10 = `5`*2` * 9 * 8 * 7 * 6 * `5` * 4 * 3 * 2 * 1). But, we are not done here. In numbers like 25, we have 2 5's {25 = 5 * 5}. So 25!(`25=5*5` * 24 * 23 * .... * 1) will have 5+1=6 5's.
        number_of_trailingZeroes, k = 0, 5
        while k <= n:
            number_of_trailingZeroes += n // k
            k *= 5
        return number_of_trailingZeroes