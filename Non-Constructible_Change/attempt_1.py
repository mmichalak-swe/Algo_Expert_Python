# O(nlogn) time | O(1) space

def nonConstructibleChange(coins):
    if not coins:
        return 1
	
    coins.sort()
	
    if coins[0] != 1:
        return 1
	
    current_change_created = 0;
	
    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1
		
        current_change_created += coin

    return current_change_created + 1
