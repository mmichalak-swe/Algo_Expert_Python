# NOT MUTATING EXISTING ARRAY
# def threeNumberSort(array, order):
# 	counts = (array.count(order[0]), array.count(order[1]), array.count(order[2]))
    
# 	ans = []
# 	for i in range(3):
# 		for j in range(counts[i]):
# 			ans.append(order[i])
    
# 	return ans

# MUTATING EXISTING ARRAY
def threeNumberSort(array, order):
    counts = (array.count(order[0]), array.count(order[1]), array.count(order[2]))

    sub_count_idx = 0
    sub_count = 0

    for i in range(len(array)):
        while (counts[sub_count_idx]) == 0:
            sub_count_idx += 1
        if sub_count == counts[sub_count_idx]:
            sub_count_idx += 1
            while (counts[sub_count_idx]) == 0:
                sub_count_idx += 1
            sub_count = 0
        array[i] = order[sub_count_idx]
        sub_count += 1

    return array
