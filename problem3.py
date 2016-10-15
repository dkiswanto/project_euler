n = 600851475143
i = 1

prime_factor = []

while i < n:
    prime_num = True

    if n % i == 0:

        j = 2
	while j < i:
	    if i % j == 0:
		prime_num = False
		break

	    j += 1

	if prime_num:
	    print i
	    prime_factor.append(i)

    i += 1


print "done"
