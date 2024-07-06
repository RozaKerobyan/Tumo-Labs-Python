tuples_list = [(1,2,3), (4,4,4), (7,2,2)]

max_sum_tuple = max(tuples_list, key=lambda x: sum(x))

print(max_sum_tuple)
