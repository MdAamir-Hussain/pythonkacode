def is_prime(num, divisor= None):
	if num <= 1:
		return False
	if divisor is None:
		divisor = num -1
	if divisor ==1:
		return True
	if num % divisor ==0:
		return False
	return is_prime(num, divisor-1)


def primes_in_range(start, end):
	if start > end:
		return []
	if is_prime(start):
		return [start] + primes_in_range(start+1, end)
	return primes_in_range(start+1,end)



start =10
end = 50

print(f"Prime numbers between {start} and {end} : {primes_in_range(start,end)}")