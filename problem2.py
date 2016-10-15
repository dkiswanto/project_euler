n_before = 1
n = 1

sum_even_val = 0

seq_num = 0

while seq_num < 4000000:
    temp = n + n_before
    if temp % 2 == 0:
	seq_num += temp

    n_before = n
    n = temp

print seq_num


