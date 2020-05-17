def factorial(n):
# Input: n, a non-negative integer
# Output: return n!
	if n == 0:
		return 1, 1
	else:
		result = 1
		for i in range(1,n+1):
			result = result * i
	num1 = n
	return result, num1

def addFactorial(n):
# Input: n, a non-negative integer
# Output: 0!+1!+…,+n!
	sum = 0
	for i in range(n+1):
		a,b =factorial(i)
		sum += a

	num2 = n*(n+1)/2
	return sum, num2
for i in range(20):
	sum, num2 = addFactorial(i)

	result, num1 = factorial(i)

	part1 = '{0:<3}'.format(str(i) + '!')+'='
	part2 = '{0:<23}'.format('= ' + str(result))
	part3 = '{0:<18}'.format('no.multi. ='+str(num1))
	part4 = '{0:<11}'.format('sum of '+str(i)+'!')
	part5 = '{0:<24}'.format('= ' + str(sum))
	part6 = '{0:<15}'.format('no.multi. ='+str(int(num2)))
	print( part1+part2+part3+part4+part5+part6 )
print()
print()
'''
b)

Key: n*(n+1)/2

Explanation:
Every time when we invoke factorial(n), we will do n times multiplications. When we invoke addFactorial(n), we will start
from factorial(0) to factorial(n), which means that we need to do 1 + 2 + 3+ ... + n times of multiplications. As a result,
the answer is n*(n+1)/2. 

'''
def new_addFactorial(n):
# Input: n, a non-negative integer
# Output: 0!+1!+…,+n!
	sum = 0
	list = [1]
	k = 1
	fac = 1
	while k <= n:
		fac = fac * k
		list.append(fac)
		k = k + 1
	for i in list:
		sum += i
	return sum, k-1

for i in range(20):
	sum1, num2 = addFactorial(i)
	sum2, num2new = new_addFactorial(i)
	part1 = '{0:<5}'.format(str(i) + '!')+':'
	part2 = '{0:<45}'.format('the old addFactorial:' + str(sum1))
	part3 = '{0:<8}'.format(int(num2))
	part4 = '{0:<45}'.format('the new addFactorial:'+str(sum2))
	part5 = '{0:<24}'.format((num2new))
	print(part1+part2+part3+part4+part5)
new_addFactorial(19)

'''
Key: n
Explaination:
When we invoke new_addFactorial this time, every time we do a multiplication, we append the
value to a list. In this way, we only need to do n times multiplications. At last, we add up 
the values in the list. Actually, every time we have used previous results which make the 
time complexity lower.
'''
