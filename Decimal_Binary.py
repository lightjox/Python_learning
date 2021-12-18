# use Recursion for Decimal to Binary
def tento2 (n):
    lt = []
    def func(n):
        if  n == 1 :
            lt.append(1)
        else:
            tento2( n//2 )
            lt.append( n%2 )
        return lt
    return func(n)

tento2(600)

#Binary to Decimal
def bito10(lt):
    def func(lt):
        ans = 0
        for i in range(len(lt)):
            if lt[i] == 1:
                ans += (2 ** (len(lt) -1 - i))
        return ans
    return func(lt)
x = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]

bito10(x)
