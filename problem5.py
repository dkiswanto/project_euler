check_num = 20 #start with 20
found_smallest = False

while not found_smallest:
    n = 20
    while n > 1:
	if check_num % n != 0:
	    break
	if n == 2:
	   found_smallest = True
	n -= 1

    print check_num
    check_num = check_num + 20
