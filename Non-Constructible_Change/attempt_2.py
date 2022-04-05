# O(nlogn) time | O(1) space

def nonConstructibleChange(coins):
	
    coins.sort()
	
    current_change_created = 0;
	
    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin

    return current_change_created + 1
